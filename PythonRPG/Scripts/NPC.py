import pygame
import random
from PythonRPG.Scripts.Timer import *
from PythonRPG.Scripts.globals import *

pygame.init()


def get_faces(sprite):
    faces = {}
    size = sprite.get_size()
    tile_size = (int(size[0] / 2), int(size[1] / 2))

    south = (pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA))
    north = (pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA))
    east = (pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA))
    west = (pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA))

    south.blit(sprite, (0, 0), (0, 0, tile_size[0], tile_size[1]))
    north.blit(sprite, (0, 0), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
    west.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
    east.blit(sprite, (0, 0), (0, tile_size[1], tile_size[0], tile_size[1]))

    faces["south"] = south
    faces["north"] = north
    faces["west"] = west
    faces["east"] = east

    return faces

def moveNPC(npc):
    npc.facing = random.choice(("south", "north", "east", "west"))
    npc.walking = random.choice((True, False))

class NPC:

    AllNPCs = []

    def __init__(self, name, pos, dialog, sprite):
        self.name = name
        self.X = pos[0]
        self.Y = pos[1]
        self.Dialog = dialog
        self.Width = sprite.get_width()
        self.Height = sprite.get_height()
        self.walking = False
        self.Timer = Timer(1)
        self.Timer.OnNext = lambda: moveNPC(self)
        self.Timer.Start()

        # Get NPC Faces
        self.facing = "south"
        self.faces = get_faces(sprite)

        # Publish
        NPC.AllNPCs.append(self)

    def Render(self, surface):
        self.Timer.Update()
        if self.walking:
            move_speed = 100 * Globals.deltatime
            if self.facing == "south":
                self.Y += move_speed
            if self.facing == "north":
                self.Y -= move_speed
            if self.facing == "east":
                self.X += move_speed
            if self.facing == "west":
                self.X -= move_speed

        surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))


class Male1(NPC):

    def __init__(self, name, pos, dialog=None):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics\\NPC\\male1.png"))






