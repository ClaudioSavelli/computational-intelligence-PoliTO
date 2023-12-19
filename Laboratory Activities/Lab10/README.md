# Task

Use reinforcement learning to devise a [*tic-tac-toe*](https://en.wikipedia.org/wiki/Tic-tac-toe) player.

# Solutions proposed

## Basic problem 

## Generalisation of the problem also on O 



# Results

All the results below are obtained by averaging the results of 10_000 games. 

## Basic problem



## Generalisation of the problem also on O

## Hyperparameter Tuning 




### Training Time 

Augmenting the number of training steps also the time required to train the model increases. The following table shows the average time required to train the model for different number of training steps.

| Training Steps | Time (s) |
|----------------|----------|
| 125_000            | 21      |
| 250_000           | 42      |
| 500_000          | 82     |
| 1_000_000         | 165    |

### Table of Results

The following tables shows the results obtained by training the model for different number of training steps.

#### Agent vs. Random



#### Random vs. Agent




# Conclusions
The outcomes detail the implementation of diverse approaches in the game of Nim. Evolutionary strategies, denoted as ES1, ES2, and ES3, were employed with varying combinations of move selection methods. Notably, ES3, which integrates an expert_system, falls short of achieving the optimal strategy outlined in task 2.1 and lags behind the effectiveness demonstrated by the Monte Carlo strategy.

The Monte Carlo Strategy stands out for its remarkable performance, consistently attaining high win rates across all scenarios. Its superiority is evident as it consistently outperforms both casual play and specific strategies such as Gabriel and Optimal. This underscores the strategy's efficacy in navigating the intricacies of the Nim game.

The final experiment highlights the near-universal success of the Monte Carlo strategy when pitted against the Evolutionary Strategy. This further emphasizes the potency of the Monte Carlo approach in outperforming alternative strategies, including those driven by evolutionary algorithms.