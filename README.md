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

Process:



Image and sound effect sources:
Spaceship sprite: Opengameart.org, author “scofanogd”
Space background sprite: Opengameart.org, author “cuzco”
Bullet sprite: Opengameart.org, author “Bonsaiheldin
