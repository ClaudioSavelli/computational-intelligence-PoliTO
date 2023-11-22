# Lab2 Reviews - Claudio Savelli (S317680)

## Review 1 - Florentin Udrea

### Link

https://github.com/florentin1304/computational-intelligence/issues/3

### Text

Starting with the structure and clarity of the code, I think your code is very clear and easy to read, also thanks to the notebook structure. The only note I want to make is that I would have increased the number of comments or markdowns by perhaps removing those lines of code that have been commented out creating a sense of clutter. Also, the graphs are quite clear once the code is analysed, I would have added only a title and information about the axes to allow an immediate visualisation of them.

As for the methodologies followed, I find your multiple approaches to the problem very interesting, it would have been even more interesting to see how the three methods you proposed would have played with each other, to get a further degree of comparison.

In all the methods, I was very impressed by the strategy for mutations that incorporate a decreasing standard deviation of the Gaussian as generations progress, balancing exploration and exploitation. This approach, in fact, allows for the exploration of a diverse solution space early on and refines the solutions as the algorithm converges, leading to more precise adaptations.

To conclude, the method that impressed me the most is certainly the neural network one, since in your solution you mix the idea of evolutionary algorithms with that of a neural network very well in my opinion, exploiting the strengths of the two strategies to the full. I found it very interesting to use the weights of a neural network as genomes that can be mutated. I would perhaps have considered other types of mutation in this part to see the effects, instead of just changing the weights of one layer each time.

Having said that, I find your work very well done and I thank you for introducing me to the world of Neuroevolution!

## Review 2 - Mattia Sabato

### Link

https://github.com/Mattizza/Computational_Intelligence_2023-2024/issues/9

### Text

Starting with the clarity of the proposed notebook, I find the theoretical description of the problem you faced, and what led you to make each choice during the development of the lab, extremely interesting and comprehensive. I also find very interesting the personal comments and criticisms that you made in the notebook, turning the lab into a kind of lecture.
My only note to the code is that it would have been useful to comment on it more to make it easier and smoother to read, but after a first glance, it is easy to interpret and understand how it works.

While it is true that Nim-Sum was used for fitness evaluation, which, as you also say, is not really legal considering that it leads to an exact solution, I very much appreciated how you exploited the latter to evaluate the opponent's best move within each iteration, not just analysing the state of the game but creating a sort of strategy that puts together an evolutionary algorithm and a sort of Minimax, playing considering the opponent's best possible moves.

On the other hand, I found the graph extremely interesting and clear, which compares the wins obtained against a given opponent by changing the population size and, as expected, as the population size increases, the percentage of games won also increases.
A question comes to mind regarding the last comment you made in the conclusion:
"Remember that higher values do not always result in higher performance, and that there could be threshold value characteristic of the problem after which any increment may be detrimental."
in fact, over an infinite number of matches, shouldn't it be assured to get an improvement by increasing the population considering that the fitness is "perfect"?

In conclusion, I find your work very valuable and interesting, a source of numerous insights!