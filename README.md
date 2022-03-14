# Clash-of-Cans
A python game similar to clash of clans
Built from scratch in Python using principles of Object Oriented Programming such as Inheritance, Polymorphism, Encapsulation, and Abstraction.

To play the game, run

``` python game.py```

- press q to quit the game.
- press w,a,s,d to control the King.
- press p, o, i to spawn barbarians in the spawn points displayed. 
- press u to spawn a wallbreaker
- press r to use the rage spell
- press h to use the heal spell

To watch the replay of a game, run 

``` python replay.py ./replays/x```  # (x is the replay file name)

# Instructions 

- The game starts with a village with few buildings, namely the Townhall, Huts, Cannons and walls surrounding them.
- The objective is to destroy the village using your army, which consists of a King and Troops such as Barbarians and wallbreakers. 
- Use one of the spawn points to deploy your troops.
- there are two kinds of troops, Barbarians and wallbreakers, barbarians attack any building they come in contact with, wallbreakers blast only walls, and also die in the process. 
- The King can be controlled using the WASD keys, use space bar to attack any single building, and use e for an AOE attack which attacks any building within a radius of 3 tiles from the king.
- There are two spells:
    - rage, which makes your troops and king faster and stronger.
    - heal, which heals your troops and king.
