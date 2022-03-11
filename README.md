# Clash-of-Cans
A python game similar to clash of clans

To play the game, run

``` python game.py```

- press q to quit the game.
- press w,a,s,d to control the King.
- press p, o, i to spawn barbarians in the spawn points displayed. 
- press u to spawn a wallbreaker

To watch the replay of a game, run 

``` python replay.py ./replays/x```  # (x is the replay file name)

Bonus implemented:

1. There is a limit on the number of barbarians you can spawn. (20)
2. Troop has a dimension "direction" which changes according to movement input (w,a,s,d), the troop's normal attack will be in this direction 
3. Wallbreaker troop: The troop goes to the closest wall, and damages the walls around it, and self destructs
