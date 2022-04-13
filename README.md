# Clash-of-Clans
A python game similar to clash of clans
Built from scratch in Python using principles of Object Oriented Programming such as Inheritance, Polymorphism, Encapsulation, and Abstraction.

To play the game, run

``` python game.py```

- press q to quit the game.
- press w,a,s,d to control the Hero(King or Queen).
- press any key from 1 to 9 to spawn troops in the spawn points displayed. 
  - 1 to 3 spawn barbarians in 3 different spawn points
  - 4-6 spawn archers
  - 7-9 spawn balloons

- press r to use the rage spell
- press h to use the heal spell

To watch the replay of a game, run 

``` python replay.py ./replays/x```  # (x is the replay file name)

# Instructions 

- The game starts with a village with few buildings, namely the Townhall, Huts, Cannons, Wizard Towers and walls surrounding them.
    - Cannon: defensive building which attacks any troop which is on the ground.
    - Wizard Tower: defensive building which can attack even aerial troops like balloons, also does AOE damage. 
- The objective is to destroy the village using your army, which consists of a Hero (King or Queen, you can choose!) and Troops such as Barbarians, Archers and Balloons. 
- There are three levels in the game, each with more number of defensive buildings. 
- Use one of the spawn points to deploy your troops.
- there are four kinds of troops, Barbarians, Archers, Balloons and WallBreakers
    -  barbarians attack any building they come in contact with
    - wallbreakers blast only walls, and also die in the process. 
    - archers can attack with a range, like outside of walls
- The Hero can be controlled using the WASD keys, use space bar to use a normal attack and 'e' for a special attack. Player can choose between King and Queen at the beginning of a game.
    - King : normal attack is similar to barbarian where he attacks a single building with his sword, special attack is an AOE axe attack which damages buildings around him.
    - Queen: normal attack is an AOE attack which deals damage to buildings at a distance in which the Queen is facing, special attack is also an AOE attack with much more range and damage radius, which is executed with a 1 second delay due to its charging up. 
- There are two spells:
    - rage, which makes your troops and king faster and stronger.
    - heal, which heals your troops and king.


