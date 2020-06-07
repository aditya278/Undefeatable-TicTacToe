# Undefeatable-TicTacToe
A Small python console program which lets you play a game of TicTacToe with an AI opponent who is practically undefeatable.

The AI is made using the MiniMax algorithm. The MiniMax algorithm is a kind of Backtracking algorithm which is used in decision making and game theory to find the optimal move for a player, assuming that the opponent is playing it's turn optimally.

The two players in a MiniMax algorithm are called Maximizer and Minimizer. The goal of the maximizer is to move at such place where the the score will be maximum and the goal of the minimizer is to play the move such the the score is the minimum.

In this code, the AI follows the same set of conditions. The call to the MiniMax method is recurssive, i.e. the AI will compute all the possible moves using backtracking approach. The move which will provide the most optimal path such that the score of the AI is always the heighest will be chosen. As the AI has already predicted the best moves of the player, the game will either be a Draw or the AI will be the winner. 
