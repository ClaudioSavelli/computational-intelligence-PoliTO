# Lab10 Reviews - Claudio Savelli (S317680)

## Review 1 - Lorenzo Greco

### Link

https://github.com/loregrc/Computational-intelligence/issues/4

### Text


Hello again! I saw your Lab10 and was very interested, so I decided to review your work! 

Starting with the writing and structure of the code, I found it excellent to divide each method into its own cell with a title, making easy to understand the purpose each function had within your workflow. The only thing I have to say about this is that it would probably have been preferable to write general functions that were valid whether the agent played first or second (or both), thus avoiding writing a lot of unnecessary code and making the work less verbose. This could easily be achieved by passing the two players to `intelligent_game` (rather than `intelligent_game_X` or `intelligent_game_O`). 

As for the experiments you carried out, I found them very interesting and really complete. I appreciated how you put the whole workflow you followed inside the README, pointing out its strengths and weaknesses, making the analysis of the work extremely more immediate and clear, so much so that it seemed as if I were working with you! 

Another plus point is that you not only limited yourself to optimising the agents against a random player but also trained them to play against optimal tic-tac-toe players, forcing a draw every time, even going beyond the laboratory objectives!

The only note I want to make about the experiments is the number of games played during the training phase. In fact, you could have considered, instead of increasing the number of training games from 100,000 to 500,000, which also means slowing down the training time, exploiting the nature of the tic-tac-toe table! In fact, for each position in the play, there can be up to 4 totally identical positions by simply rotating the board (unless the first move is 'X' in the middle). In this way you don't only decrease the number of games to be played by a factor of 3 but also ensures that you see more states in large numbers so that the value dictionary covers all possible positions more evenly.

In conclusion, I think the work is superb, perfectly covering not only the required objectives but also going beyond them, with a neat code accompanied by an excellent description. Great job!



## Review 2 - Beatrice Occhiena

### Link

https://github.com/beatrice-occhiena/Computational_intelligence/issues/6

### Text


Hi Beatrice!!! Seeing several lab 10 works, I found yours and, having found it very interesting, I decided to make it a review. 

First of all, I wanted to congratulate you on the neatness of the notebook, which allows, also thanks to its descriptive comments, to understand the code easily without a README. The methods are written clearly and are easy to comprehend. I also found the emojis to print the board very pretty, and I thank you because I did not know about this feature of Jupyter that I will use in the future! 

In addition, I wanted to emphasize how the theoretical explanations you carry out along the notebook are not only useful for an immediate and easy understanding of the code but also turn your work into a tool that can teach the application of the Monte-Carlo method in Reinforcement Learning even to those who are novices in the field! In fact, not only are the explanations extremely clear and concise, but you perfectly point out all the positive and negative aspects of applying this method to any reinforcement learning approach. Excellent work! 

I also found very useful the two graphs you proposed, which show how the win rate varies as the number of training games played varies. This shows easily the difference in when our agent does or does not start the game first.

To conclude, the most interesting part of the code, in my opinion, is the one related to *'Symmetry Recognition'*. I have also carried it out with a different approach. In my proposed method, I transformed each training match played the trajectory of the match into four equivalent trajectories, rotating the board 90 degrees each time. In such a way, the four trajectories generated for each match are used for training. This method was possible because of the simplicity of the problem, but in this way, the space occupied by the dictionary is not reduced, which is the case in your solution. 

As for your request, I could not find an immediate solution to your problem, which seems to make sense the way you try to return to the canonical state. I am sorry ☹

I think you did a great job, and I enjoyed reading it and being able to review it. Congratulations! 

