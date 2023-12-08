# Lab9 Reviews - Claudio Savelli (S317680)

## Review 1 - Lorenzo Greco

### Link

https://github.com/loregrc/Computational-intelligence/issues/2

### Text


Starting with the structure and clarity of the code, I think your notebook is elegant and easy to follow. Thanks to the numerous markdowns, comments and the extremely explanatory README the reader can immediately understand the main steps of the Lab and how they were processed. The only note I would like to make is regarding the presentation of the results, where I would advise you to make the best solution obtained with each instance of the problem more visible (You have indeed highlighted it within the output file, but it is 2000+ lines). Moreover, even the graph, which could be very interesting to analyse, partially loses its usefulness if which combination of parameters each point goes back to isn’t traced. Having said that, I really compliment you on the overall clarity!

As far as the code is concerned, I seem to have found a dissimilarity between what is written in the README and the notebook. In fact, within the code, it seems to me that no tournament method (taking a random subset of individuals each time and choosing from those the best one) is used to select the parents for each generation, but simply from the best (elite), two parents are randomly and iteratively sampled and generated from those an offspring. This method I imagine could easily incur a local minimum, considering that at each generation potentially the elite could vary very little.

Also, for the reason just mentioned, as a possible improvement that would probably drastically decrease the number of fitness calls used I would suggest you try using memoisation, i.e. saving locally the results obtained by evaluating the fitness function on a particular gene, not having to call it again when you need to review it. Furthermore, it might be useful to add a stopping criterion, to stop the generation in case for many consecutive iterations the best solution(s) does not change.

Another aspect that aroused my interest was the mutation function. I found your very exploratory approach very interesting, considering that with the maximum ’mutation_rate’ value about 10% of the solution changes for each offspring. Most likely the best hyperparameter was the lowest one precisely because even once you got close to the solution you were mutating your gene too much, moving away from the minimum and thus continuing to choose elite elements. I would advise you to try a hybrid approach, keeping the mutation rate high during the first generations (exploration), and then gradually lowering it in the final ones (exploitation)!

Overall, I think you did a great job generating a clear, formative and effective solution. Reading your README made me curious about the other approaches you tried before this one, you could have mentioned them! Thank you for the interesting insights! Until next time!



## Review 2 - Filippo Bertolotti

### Link

https://github.com/filippobertolotti0/my_computational_intelligence_317811/issues/3

### Text


Starting with the structure and clarity of the code, the code is very minimal, not very verbose, and easy to read, also because you have commented on each function. Excellent work!

Furthermore, the README is very explicative and clear and gives an immediate idea of the work done and the procedures followed. It would have been interesting to try to carry out more experiments, perhaps even reporting them in the README file without keeping them only in the notebook.

As far as the results obtained are concerned, the number of generations to reach the solution in Problem Instance 1 should certainly be emphasised, this is probably due to the lack of dynamism within the code, which always behaves in the same way at any stage of the search, not trying to increase exploration or exploitation when necessary. In addition, the method used to conclude the search could lead to the calling of numerous fitness functions unnecessarily even though it is the purpose of the challenge.

Another interesting point that could be analysed is concerning parent selection, where it might have been interesting to try to choose the parents with higher probability scores (tournament or roulette method). One has a kind of proxy for this behaviour by removing half of the worst parents before the crossover phase. Moreover, the mutation is probably also quite intensive, especially if applied in the same way throughout the whole research phase, and not only in the initial one. On the other hand, I found the use of Gaussian mutation very interesting. The applied crossover is also very interesting.

In conclusion, the work done is interesting even though it could very easily run into a local minimum. On the other hand, I congratulate you on the work you have done! See you next time!

