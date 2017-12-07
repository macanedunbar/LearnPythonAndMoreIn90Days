import pygame
from PythonRPG.Scripts.NPC import *

pygame.init()

class Player:

    def __init__(self, name, level):
        self.name = name
        self.facing = "south"
        self.level = level
        self.health = 100
        sprite = pygame.image.load("Graphics\\player.png")
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]

        #get player faces
        self.faces = get_faces(sprite)

    def render(self, surface, pos):
        surface.blit(self.faces[self.facing], pos)