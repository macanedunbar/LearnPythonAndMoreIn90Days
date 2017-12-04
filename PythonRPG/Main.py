import pygame
import sys
import time
from PythonRPG.Scripts.UltraColor import *
from PythonRPG.Scripts.textures import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0
tile_size = 32

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("Graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Python RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)


def count_fps():
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        return FPS


create_window()
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # LOGIC
    count_fps()

    # RENDER GRAPHICS
    window.blit(Sky, (0, 0))

    # - Render Simple Terrain Grid
    for x in range(0, 640, tile_size):
        for y in range(0, 480, tile_size):
            window.blit(Tiles.Grass, (x, y))

    show_fps()

    pygame.display.update()

pygame.quit()
sys.exit()
