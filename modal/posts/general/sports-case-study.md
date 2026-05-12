---
title: "How a top tier European soccer team sped up their data processing and reduced costs by 50%"
author: "amritangshu"
date: "2024-12-04"
url: "https://modal.com/blog/sports-case-study"
category: "general"
site: "modal"
---

# How a top tier European soccer team sped up their data processing and reduced costs by 50%

  Since the advent of [Moneyball](https://en.wikipedia.org/wiki/Moneyball:_The_Art_of_Winning_an_Unfair_Game),
sports teams around the world have incorporated data analysis into their decision making. At Modal, we’re fortunate to
partner with one of the world’s best soccer teams in their quest to win their championship. To honor their request for anonymity,
we will be referring to them as [AFC Richmond](https://ted-lasso.fandom.com/wiki/AFC_Richmond).

![](https://modal-cdn.com/cdnbot/soccer-cv0vsttzny_8f133f35.webp)

 Image taken from [Amritangshu Mukherjee’s medium post on tracking soccer players](https://medium.com/@amritangshu.mukherjee/tracking-football-players-with-yolov5-bytetrack-efa317c9aaa4)

## The problem: Processing spatio-temporal match data efficiently

In every match, computer vision systems are deployed to produce large amounts of tracking data for every player. Typical tracking data contains x/y positions
for each of the 22 players and the ball at 25 frames-per-second, resulting in ~3.5 million observations per game. AFC Richmond was looking for a solution to ingest
their tracking data for each frame of a match, run inference on it, and write the results to cloud storage. AFC Richmond uses a custom transformer-based model that takes
as input the unstructured spatio-temporal data from sequences of play, and produces structured outputs and high-dimensional embeddings. These outputs and embeddings are
used for analyzing the performance of the players in different situations: was it the right time to take a shot? How effective was the positioning of the players during a
particular moment? How do other teams handle such situations?

Before Modal, AFC Richmond tried using a GPU cluster on a major cloud provider, but it was not well set up for this workflow and required them to choose from a
limited set of instance types. This limitation meant that AFC Richmond had to pay for larger and more powerful configurations than they needed. Furthermore, long
cluster warmup times (6-8 minutes) added to their costs and made horizontal scaling trickier than they had hoped.

## Modal’s solution: serverless batch processing on GPUs

![](https://modal-cdn.com/cdnbot/soccer-workflow5azt_811_d8df8d28.webp)

AFC Richmond decided to switch over to Modal so that their infrastructure would be more flexible to build on. They didn’t have to worry about underutilization, and containers started up
in a matter of seconds. The usage-based pricing and serverless nature of the product resulted in a 50% cost reduction for processing a full season of games.

Modal is also well set up to scale automatically based on the volume of data inputs. Using Airflow on Modal, AFC Richmond was able to achieve high parallelization,
processing data for games in a matter of minutes rather than hours.

Furthermore, the team loved the smooth developer experience; they were able to get set up and run their first job within hours:

 “Modal made it easy to install a minimal set of libraries needed for the specific workflow and provided an easy way to read/write from cloud storage.
        The ability to switch quickly between CPUs and different GPU types made testing and iterating incredibly straightforward, and the smooth web interface made it easy

## Bonus: Semantic search with embeddings

AFC Richmond also built a lightweight in-memory vector DB on top of Modal, as this turned out to be cheaper than using managed vector DB solutions. This allowed them to make queries
based on the semantic similarity of embeddings generated in the previous steps. As an example: coaching staff can take a particular moment of a match and query for similar situations
that showed up in a different match to determine the best course of action for the players.

We’re excited to partner with AFC Richmond to develop more use cases and are honored that we can indirectly deliver joy to millions of soccer fans around the world.