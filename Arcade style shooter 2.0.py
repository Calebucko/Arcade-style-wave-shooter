# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:45:01 2024

@author: Caleben Jahn
"""

import pygame, simpleGE, random

class mainShip(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ship.png")
        self.position = (320,240)
        self.size = (10,10)
        self.moveSpeed = 5
        self.setBoundAction(self.STOP)

    
    def process(self):
        if self.isKeyPressed(pygame.K_a):
           # self.x -= self.moveSpeed
            self.imageAngle += 5
        if self.isKeyPressed(pygame.K_d):
            #self.x += self.moveSpeed
            self.imageAngle -= 5
        if self.isKeyPressed(pygame.K_s):
            self.y += self.moveSpeed
        if self.isKeyPressed(pygame.K_w):
            #self.y -= self.moveSpeed
            self.forward(self.moveSpeed)
        if self.isKeyPressed(pygame.K_j):
            self.scene.currentbullet
            self.scene.Bullet.shoot()
        
    
#class explosion(simpleGE.Sprite):
 #   def __init__(self, scene):
  #      super(). __init__(scene)
   #     self.setImage("explosion.png")
        
            
            
class enemyShip(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("enemyShip.png")
        self.position = (random.randint(1,600), random.randint(1, 450))
        self.size = (10,10)
        self.moveSpeed = 2
        
    def process(self):
        playerPosition = self.scene.mainShip.position
        angle = self.dirTo(playerPosition)
        self.setAngle(angle)
        self.forward(self.moveSpeed)
        

        
    
    

class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.colorRect("green", (4,4))
        self.setBoundAction(self.HIDE)
        self.hide()
        
    def shoot(self):
        self.show
        self.position = self.parent.position
        self.moveAngle = self.parent.imageAngle
        self.speed=25
    
    
            
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__((740, 580))
        self.setImage("Space.jpg")
        
        
        
        self.mainShip = mainShip(self)
        #self.explosion =explosion(self)
        self.enemyShip = enemyShip(self)
        self.enemyShips = []
        self.enemyShipnumber = 8
        for i in range(self.enemyShipnumber):
            self.enemyShips.append(enemyShip(self))
        self.Bullet = Bullet(self, self.mainShip)
        self.bullets = []
        self.bulletnumber = 10
        self.currentbullet = 0
        for i in range(self.bulletnumber):
            self.bullets.append(Bullet(self, self.mainShip))
        self.sprites = [self.mainShip, self.Bullet, self.enemyShips]
    
        #for Bullet in self.bullets:
         #   if self.enemyShip.collidesWith(Bullet):
          #      self.explosion = self.enemyShip
          
class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Space.jpg")
        self.choice = "Play"
        
        self.instructions =simpleGE.MultiLabel()
        self.instructions.textLines = [
            "You're controlling a space ship, and enemy ships are closing in on you"
            "Shoot the enemy ships, and don't let them hit you, or the game is over"
            "W to move up, A to move left, D to move right, S to move down"]
        self.instructions.size = (650 , 300)
        self.instructions.center = (360, 290)
        
        self.quitbutton=simpleGE.Button()
        self.quitbutton.text = "Quit"
        self.quitbutton.center= (500,350)
        
        self.playbutton = simpleGE.Button()
        self.playbutton.text = "Play"
        self.playbutton.center= (200, 350)
        
        self.sprites = [self.instructions, self.quitbutton, self.playbutton]
        
        def process(self):
            if self.quitbutton.clicked:
                self.choice = "Quit"
                self.stop()
            if self.playbutton.clicked:
                self.choice = "Game"
                self.stop()
         
            
        
        
            
        
def main():
    keepGoing= True
    while(keepGoing):
        instructions = Instructions()
        instructions.start()
        if instructions.choice == "Play":
            game = Game()
            game.start()
        else:
            keepGoing = False
if __name__ == "__main__":
    main()