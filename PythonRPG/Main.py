import pygame
import sys
import time
import math
from PythonRPG.Scripts.UltraColor import *
from PythonRPG.Scripts.textures import *
from PythonRPG.Scripts.globals import *
from PythonRPG.Scripts.map_engine import *
from PythonRPG.Scripts.NPC import *
from PythonRPG.Scripts.player import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0

terrain = Map_Engine.load_map("maps\\smiley.map")



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
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS


create_window()

player = Player("DefaultPlayer", 1)
player_w, player_h = player.width, player.height
player_x = (window_width / 2 -player_w /2 -Globals.camera_x) / Tiles.Size
player_y = (window_height / 2 -player_h /2 -Globals.camera_y) / Tiles.Size


isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.facing = "north"
                Globals.camera_move = 1
            elif event.key == pygame.K_s:
                player.facing = "south"
                Globals.camera_move = 2
            elif event.key == pygame.K_a:
                player.facing = "west"
                Globals.camera_move = 3
            elif event.key == pygame.K_d:
                player.facing = "east"
                Globals.camera_move = 4
        elif event.type == pygame.KEYUP:
                Globals.camera_move = 0

    # LOGIC
    if Globals.camera_move == 1:
        if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
            Globals.camera_y += 300 * deltatime
    elif Globals.camera_move == 2:
        if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
            Globals.camera_y -= 300 * deltatime
    elif Globals.camera_move == 3:
        if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
            Globals.camera_x += 300 * deltatime
    elif Globals.camera_move == 4:
        if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
            Globals.camera_x -= 300 * deltatime

    player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
    player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size


    # RENDER GRAPHICS
    window.blit(Sky, (0, 0))
    window.blit(terrain, (Globals.camera_x, Globals.camera_y))
    player.render(window, ((window_width /2 - player_w /2), (window_height /2 - player_h/2)))


    show_fps()

    pygame.display.update()

    count_fps()


pygame.quit()
sys.exit()
