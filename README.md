# Sudoku Solver


> It is an important *recursive* strategy.

<p align="justify">
A backtracking algorithm tries to construct a solution to a computational problem incrementally, one small piece at a time. Whenever the algorithm needs to decide between multiple alternatives to the next component of the solution, it recursively evaluates every alternative and then chooses the best one.
</p>

> At its core, this algorithm is just a depth-first search of the game tree.

> Equivalently, the game tree is the recursion tree of the algorithm !

### When to apply *BackTracking* ?
-----------------------------------

- Knowledge of Rules of the Game in Question
- No randomness or hidden information that would end after a finite number of moves
    - Meaning : if we drop someone into middle of a game, and it is possible to win against another perfect player, the algorithm will tell how to win.

### Game Tree
--------------

A *state* of the game consists of the locations of all the pieces and the identity of the current player. These states can be connected into a ***game tree***, which has an edge from state *x* to state *y* if and only if the current player in state *x* can legally move to state *y*. The root of the game tree is the initial position of the game, and every path from the root to a leaf is a complete game. 



To navigate through this game tree, we recursively define a game state to be **good** or **bad** as follows:

- A game state is "good" if either the current player has already won, or if the current player can lead the opposing player into a bad state.
- A game state is "bad" if either the current player has already lost, or if every available move leads the opposing player into a good state.

Let's define **good** and **bad** states for non-leaf nodes :

- A non-leaf node in the game tree is good if it has all good children. ( By induction, any player that finds the game in a good state on their turn can win the game, even if their opponent plays perfectly. )
- A non-leaf node in the game is bad if it has at least one bad child. ( On the other hand, starting from a bad state, we can only win if the opponent makes a mistake. )


### Simple BackTracking Algorithm
----------------------------------

```python
def PlayAnyGame(X, player):
	if player has already won in state X:
		# We Won
		return Good

	if player has already lost in state X:
		# We Lost
		return Bad

	for all legal moves X to Y:
		if PlayAnyGame(Y, -player) is Bad:
			# X to Y is a good move.
			return Good

	# There are no good moves.
	return Bad			
```

  At its core, all game-playing programs are ultimately based on this simple backtracking strategy. However, since most games have an enormous number of states, it is not possible to traverse the entire game tree in practice. Instead, game programs employ other heuristics to *prune* the game tree, by ignoring states that are obviously good or bad, or at least better or worse than other states, and/or by cutting off the tree at a certain depth ( or *ply ) and using a more efficient heuristic to evaluate the leaves.*
