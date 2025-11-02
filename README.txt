Cat Jumper Game
================

Author: Viktorija Angelovska

Project description:
-------------------
Cat Jumper is a 2D platformer game where you control a cat navigating a series of platforms. The goal is to collect rats
to increase your score while avoiding jellyfish, which decrease your points. Collecting five rats triggers the win screen,
while letting your score drop to zero ends the game. The game features a main menu with options to start the game, toggle
music on or off, and exit. The gameplay includes moving platforms that the cat can jump on, and all characters, including
the player, rats, and jellyfish, have frame-based animations to create a lively environment. The background subtly changes
color over time, giving a dynamic visual effect. Sound effects and background music enhance the overall experience and provide
feedback for collecting rats, touching jellyfish, and jumping. Collision detection uses Rect objects to ensure accurate interactions
between the player, platforms, and enemies. Sprite animations use frame sequences for movement and idle states. The jellyfish cycles
through multiple frames to create animation effects, and its images have been scaled down to fit the screen without affecting collision
detection. Sound and music files are included in the sounds and music folders. Overall, the game demonstrates object-oriented programming principles,
collision detection, and basic animation logic, providing a complete and interactive platformer experience.

Classes:
--------
- Game: manages the main game loop, menus, win and lose conditions, drawing, and updating all actors.
- Player: controls the cat’s movement, jumping, gravity, horizontal velocity, animation, and collision detection with platforms and enemies.
- Rat: represents a collectible enemy that spawns at random positions within a fixed area and increases the player’s score when collected.
- Jellyfish: represents a hazard that spawns at random positions, decreases the player’s score on collision, and cycles through animation frames.
- PlatformManager: manages both static and moving platforms and detects collisions between the player and platforms.

Libraries Used:
---------------
- Pygame Zero
- random
- Rect from Pygame (for collision rectangles)

How to Run:
-----------
1. Install Python 3.13
2. Install Pygame Zero
3. Open terminal in the project folder
4. Run the game by typing: `pgzrun main.py`

Notes:
------
Sprite animations use frame sequences for movement and idle states. Background music and sounds are
included in the music and sounds folders. All code is written independently and demonstrates object-oriented
programming principles, collision detection, and animation logic.
