# Arcade-style-wave-shooter
Arcade style wave  shooter

Concept: A time pilot like arcade game where you move around the screen and have to kill various waves of enemies with different attacks. This will obviously require a lot of focus on projectiles in computer programming, as well as learning how to move between various stages or waves of the game seamlessly. Later I would also want to introduce new attacks from the enemies so there's more to keep track of and about. 
Once the game starts, an instructions screen like this will show up. The only buttons will be start and quit. Start puts them in the game state, quit closes the program.
When the game starts, the player will be in the middle of the screen, and enemies will be moving towards the player's position from the outside edges. The player and enemies will dogfight it out, while new enemies sprinkle in as more enemies die. Once all the enemies are destroyed, the wave will be over, and a new one will begin, preceded by a label that says wave 2, where the main player ship will be set back at the center of the screen, and it starts over again, but now there are more enemy ships. The game ends when the player dies or they reach the end of the three waves. The player can die from a single hit of a bullet, or by colliding into enemy ships. 

 
The game development is going to primarily be centered around making the movement of the main ship and enemies readable and fair. There’s a lot of balancing that goes into the game, as the plan is to make every attack a one hit kill, for both enemies and the players ship. The main game will consist of trying to fight 3 waves of a set amount of enemies that increases each time. 
The primary way to balance a game like this is to make the enemies move much slower than you, or to make it so there aren’t too many enemies to fill up the screen. 


Sprite list
Main game
playership:
-Able to move omnidirectionally
-moves with wasd
-when it collides with an enemy or a bullet, it explodes
-movespeed is constant
-cannot go off screen, will simply stop on the walls

Explosion:
-replaces playership sprite when playership is destroyed
-disappears quickly, ends when game resets to title screen


enemyship: 
-cpu enemy
-moves omnidirectionally as well, but at a much slower rate
-Also explodes when colliding with ship or players bullets
-when it hits the edge of the screen it will move offscreen, hide, and reset to a different position coming back towards the character
Bullet:
-fired from both playership and enemy ship
-collides with enemies and playership and causes them to explode
-can be triggered by the j button
Instructions:
Startbutton:
Starts game when clicked, can also be triggered by spacebar
Quitbutton:
Quits program when clicked, also triggered by q
Wave # label:
-Counts up whenever player defeats all the enemies in a stage
-Resets whenever ever the player loses and is sent back to the beginning of the game. 

Instructions:
You're controlling a space ship, and enemy ships are closing in on you
Shoot the enemy ships, and don't let them hit you, or the game is over
W to move up, A to move left, D to move right, S to move down
Process:
Through the process of trying to make every aspect of my proposed game design work, I learned just how much intense detail goes into making these alogrithms work. There are so many things I had to keep track of surrounding the development of a whole game, and it was an extreme challenge. I got stuck on almost every single part of my coding process. I had lots of issues involving the movement of the two types of ships. I wanted the players ship to be able to rotate and move simultaneously, as well as for the enemy ships to move towards the player ship in a similar manner. This turned out to be extremely finnicky. Collisions also caused a lot of headaches that I couldn't really resolve. There seemed to be just one piece of code I was missing that would have made it so that collisions between things like bullets and enemy ships would actually occur. This also prevented me from using my explosion sprite, as I was unable to figure out how to replace the sprites of the ships with that when they collided with either bullets or each other. The instructions also caused issues, as I couldn't figure out how to resize or recenter text within a lable, so the instructions are mostly unreadable. But I did learn a lot more about the motion of objects in simpleGE. I think its vital I work on my the little details of coding, with all the syntax issues I struggled in fixing throughout the process. If I had a do over, I would absolutely attempt to get a real handle on how the interaction between the ships and bullets would work. There were a lot of unecessary roadblocks caused by me simply not having a full grasp on how the mechanics of these sprites moving around the screen would work. The most major change I made from the game document is that I didn't make mental waves, and I also didn't use the bullet sprite, I simply made a green rectangle to act as one. I stayed on track by sticking to the original idea of just space dog fighting.



Image and sound effect sources:
Spaceship sprite: Opengameart.org, author “scofanogd”
Space background sprite: Opengameart.org, author “cuzco”
Bullet sprite: Opengameart.org, author “Bonsaiheldin
Enemy ship sprite: "MillionthVector"
