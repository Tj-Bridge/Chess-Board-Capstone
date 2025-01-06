### Electro-Mechanical Design Capstone 2025: Virtual Chess ###

------------------------------------Project Description----------------------------------------------

Chess Players will be able to play physical chess with an opponent anywhere else in the world. You get to see the pieces move in real time as if you were playing against an opponent directly in front of you and your moves will reflect on their board! Traditional chess rules apply.


How it works:

Beginning a game -

Upon starting the game, a player will be decided to begin. When the first move is made, the piece will be moved automatically on the opponents board. This will trigger a movement sequence that will rearrange the board to its updated state.

Further Gameplay - 

After successfully capturing pieces, they will sit in the jail on the outer ends of the board. On the opponents board they will automatically move from the board and update the new pieces.

Ending the game - 

After each turn, the board will detect if checkmate has been achieved and flash a checkmate message and attempt to reset the board after 10 seconds.


---------------------------------------Psuedocode--------------------------------------------------- 

Chess Pieces:

Pawn - Can move + 2 forward on first turn, otherwise + 1 forward. Attacks diagonally.

Rook - Can move forward, backward, left, right until physically blocked. Attacks as it moves.

Bishop - Can move diagonally until physically blocked. Attacks as it moves.

Knight - Can move in an L direction (+2 forward/backward, +1 left/right or +1 forward/backward, +2 left/right)

Queen - Can move forward, backward, left, right, diagonal until physically blocked. Attacks as it moves.

King - Can move one space forward, backward, left, right, diagonal unless physically blocked or in enemy attack path.

Establish dictionary and store possible moves for each piece.


Moving Pieces (work in progress):

Pieces may be in the way of other pieces for reaching its updated position. Implement bestPath algorithm to find the least destructive path to placement. Criteria will be pieces moved and time to finish

If there is clutter and multiple pieces must be moved, utilize available jail spaces.

All pieces' current position will be tracked throughout the game for ease of object detection.


Detecting Game Finish:

The King's current position will be checked every round along with a tracked boolean that indicates if its in the enemy's attack path.

