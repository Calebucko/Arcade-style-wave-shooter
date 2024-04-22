# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:45:01 2024

@author: Caleben Jahn
"""

import pygame, simpleGE

class mainShip(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ship.png")
        self.position = (320,240)
        self.size = (20,20)
        self.moveSpeed = 5

    
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_d):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_s):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_w):
            self.y += self.moveSpeed
            
    def fireBullet(self):
        super().process()
        if self.isKeyPressed(pygame.K_j):
            self.scene.currentbullet
        self.scene.bullets[self.scene.currentbullet].fire()
            
#class enemyShip(simpleGE.Sprite):
 #   def __init__(self, scene, reset):
  #      super().__init__(scene)
   #     self.setImage("enemyShip.png")
    #    self.position = ()
    #def reset:
     #   if self.
    
    

class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("bullet.png")
        self.setBoundAction(self.HIDE)
        self.hide()
        
        def shoot(self):
            self.show
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
            self.speed=25
    
    
            
        

class Game(simpleGE.Scene):
    def __init__(self, scene):
        super().__init__()
        self.setImage("Space.jpg")
        
        self.mainShip = mainShip()
        self.bullets = []
        self.bulletnumber = 100
        self.currentbullet = 0
        for i in range(self.bulletnumber):
            self.bullets.append(Bullet(self, self.mainShip))
        self.sprites = [self.mainShip, self.Bullet]
            
        
        
            
        
def main():
    game = Game()
    game.start()
if __name__ == "__main__":
    main()