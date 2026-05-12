---
title: "How Hugging Face Is Using E2B to Replicate DeepSeek-R1"
author: "Tereza Tizkova"
date: "2025-03-31"
url: "https://e2b.dev/blog/how-hugging-face-is-using-e2b-to-replicate-deepseek-r1"
category: "announcements"
site: "e2b"
---

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67eab29b007707e9347c7566_Screenshot%202025-03-31%20at%2017.19.40.png)Figure source: [https://github.com/huggingface/open-r1](https://github.com/huggingface/open-r1)

Shortly after the release of DeepSeek-R1, Hugging Face launched the [Open R1 project](https://github.com/huggingface/open-r1) to reverse-engineer the missing pieces of DeepSeek’s data and training pipeline. 

A key part of that pipeline involves [*reinforcement learning with verifiable rewards*](https://huggingface.co/papers/2411.15124), where a large language model (LLM) is trained to solve problems that can be checked for correctness against ground-truth answers. For example, given a simple math problem like “What is 1+1?”, the LLM receives a binary reward of 1 or 0 based on whether it produces the correct answer or not. As shown by DeepSeek-R1, maximising these rewards with reinforcement learning enables LLMs to obtain robust reasoning capabilities that translate into high accuracy on various public benchmarks:

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67dbbbccc24274cca94ed1ab_0_lbGOHxWxpoEqbx0g.png)Figure source: [https://huggingface.co/papers/2501.12948](https://huggingface.co/papers/2501.12948)

For domains like mathematics, verifying whether an LLM’s output is correct can be achieved by parsing strings with libraries like [Math-Verify](https://github.com/huggingface/Math-Verify). However, for domains like [competitive programming](https://huggingface.co/papers/2502.06807), the reward is obtained by executing LLM-generated code and comparing the result against the expected outcome from a set of test cases:

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67dbbc084c5a803673f7c5ee_0_n71KhlfdrM6UBjF1.png)Figure source: [https://huggingface.co/papers/2410.02089](https://huggingface.co/papers/2410.02089)

The problem here is that executing LLM-generated code locally poses many [risks](https://huggingface.co/docs/smolagents/main/tutorials/secure_code_execution#local-code-execution); the model may accidentally produce programs that corrupt your hard drive, or worse, `rm -rf` your entire home directory! 

The solution is to use E2B Sandboxes for secure code execution! Let’s take a look at how the Hugging Face team uses Sandboxes in the Open R1 project.

## Using E2B for code execution

Hugging Face uses E2B Sandboxes as part of the reward function for code execution. During training, the LLM-generated code is executed in the isolated E2B sandboxes. Currently, this reward function targets competitive programming competitions like [CodeForces](https://codeforces.com/), where solutions are executed against a set of test cases and the overall success rate is returned as the final reward. 

> “We found E2B is a simple and cost-effective platform for this. It was extremely easy to set up.”

- Lewis Tunstall, Research Engineer at Hugging Face 

```
`def code_reward(completions, **kwargs) -> list[float]:
    """Reward function that evaluates code snippets using the E2B code interpreter.

    Assumes the dataset contains a `verification_info` column with test cases.
    """
    if not is_e2b_available():
        raise ImportError(
            "E2B is not available and required for this reward function. Please install E2B with "
            "`pip install e2b-code-interpreter` and add an API key to a `.env` file."
        )

    # TODO: add support for other languages in E2B: https://e2b.dev/docs/code-interpreting/supported-languages
    """Returns a reward function that evaluates code snippets in a sandbox."""
    evaluation_script_template = """
    import subprocess
    import json

    def evaluate_code(code, test_cases):
        passed = 0
        total = len(test_cases)
        exec_timeout = 5

        for case in test_cases:
            process = subprocess.run(
                ["python3", "-c", code],
                input=case["input"],
                text=True,
                capture_output=True,
                timeout=exec_timeout
            )

            if process.returncode != 0:  # Error in execution
                continue

            output = process.stdout.strip()

            # TODO: implement a proper validator to compare against ground truth. For now we just check for exact string match on each line of stdout.
            all_correct = True
            for line1, line2 in zip(output.split('\\n'), case['output'].split('\\n')):
                all_correct = all_correct and line1.strip() == line2.strip()

            if all_correct:
                passed += 1

        success_rate = (passed / total)
        return success_rate

    code_snippet = {code}
    test_cases = json.loads({test_cases})

    evaluate_code(code_snippet, test_cases)
    """
    code_snippets = [extract_code(completion[-1]["content"]) for completion in completions]
    verification_info = kwargs["verification_info"]
    scripts = [
        evaluation_script_template.format(code=json.dumps(code), test_cases=json.dumps(json.dumps(info["test_cases"])))
        for code, info in zip(code_snippets, verification_info)
    ]

    language = verification_info[0]["language"]

    if not all(v["language"] == language for v in verification_info):
        raise ValueError("All verification_info must have the same language", verification_info)
    try:
        rewards = run_async_from_sync(scripts, language)

    except Exception as e:
        print(f"Error from E2B executor: {e}")
        rewards = [0.0] * len(completions)

    return rewards`
```

Hugging Face chose E2B Sandboxes, the isolated cloud environments for executing AI-generated code. The environment is specialized for LLMs, making it easy, for example, to extract errors, or have the LLM reference to previously defined variables, functions, etc. Inside the E2B Sandbox, it’s easy to run code, start programs, start long-running processes, use the filesystem, upload data to the Sandbox, and download any type of file from the Sandbox.

E2B Sandboxes also fulfill important requirements:

- **Security**: E2B's use of Firecrackers by AWS for creating isolated environments is a secure way to run LLM-generated code.
- **Speed**: When a new Sandbox session is started, E2B starts a small VM in the cloud. All this takes about 150-170 ms. This is critical with methods like reinforcement learning, where one tries to minimise idle time on GPUs waiting for the rewards to be computed.**‍**
- **Price**: E2B Sandboxes are cheap to run, as single training run costs up to a few dollars of E2B.

## Integrating E2B Sandboxes in Open R1

Integrating E2B Sandboxes with Open R1’s reinforcement learning pipeline was quite straight forward and involved the following steps:

- Define a template for the LLM-code to be executed, along with the reward to be computed (success rate in the case of competitive programming)

```
`evaluation_script_template = """
import subprocess
import json

def evaluate_code(code, test_cases):
    passed = 0
    total = len(test_cases)
    exec_timeout = 5

    for case in test_cases:
        process = subprocess.run(
            ["python3", "-c", code],
            input=case["input"],
            text=True,
            capture_output=True,
            timeout=exec_timeout
        )

        if process.returncode != 0:  # Error in execution
            continue

        output = process.stdout.strip()
        all_correct = True
        for line1, line2 in zip(output.split('\\n'), case['output'].split('\\n')):
            all_correct = all_correct and line1.strip() == line2.strip()

        if all_correct:
            passed += 1

    success_rate = (passed / total)
    return success_rate

code_snippet = {code}
test_cases = json.loads({test_cases})

evaluate_code(code_snippet, test_cases)
"""`
```

- Use the asynchronous Sandbox to launch hundreds of tasks in parallel

```
`async def run_async(scripts: list[str], language: str) -> list[float]:
   sbx = await AsyncSandbox.create(timeout=30, request_timeout=3)

   # Create a list of tasks for running scripts concurrently
   tasks = [run_script(sbx, script, language) for script in scripts]

   # Wait for all tasks to complete and gather their results as they finish
   results = await asyncio.gather(*tasks)
   rewards = list(results)  # collect results

   # Kill the sandbox after all the tasks are complete
   await sbx.kill()

   return rewards`
```

> “It took just a few hours to implement E2B for code execution”

- Lewis Tunstall, Research Engineer at Hugging Face 

Important features provided by E2B are:

- **Multi-language support**. The Open-r1 project can currently run code in Python, JavaScript, C++ with more languages (e.g., Rust and Lean4) coming in the future. Support for multiple languages is possible by specifying the language inside the E2B Sandbox.
- **Sandbox persistence**. The persistence across calls was needed. E2B allows this using sandbox.run_code(). The E2B sandboxes use headless Jupyter server so the code is essentially running in a Jupyter-like notebook.
- **Handling multiple instances**. Hugging Face is currently launching **hundreds of **sandboxes per training step in their Open R1 experiments.

## What's next 

What does the Open R1 project mean for open reasoning models? Since Hugging Face collected a lot of learnings when building it, it can mean a significant improvement in the quality of open-source LLMs in the next few months.

> “We plan to scale up our reinforcement learning pipeline to target code execution feedback for models like OlympicCoder”

- Lewis Tunstall, Research Engineer at Hugging Face 

## Learn more

- [Open-r1 GitHub repository](https://github.com/huggingface/open-r1)
- [Open-r1 blog post](https://huggingface.co/blog/open-r1)
- [The R1 paper](https://arxiv.org/pdf/2501.12599v1)