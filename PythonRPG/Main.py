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
from PythonRPG.Scripts.meloonatic_gui import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0

terrain = MapEngine.load_map("maps\\testmap.map")

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("Graphics\\sky.png")
logo_img_temp = pygame.image.load("Graphics\\logo.png")
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0,0))
del logo_img_temp

Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title, clock
    window_width, window_height = 800, 600
    window_title = "Python RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE | pygame.DOUBLEBUF)
    clock = pygame.time.Clock()


def count_fps():
    global FPS
    FPS = math.floor(clock.get_fps())
    if FPS > 0:
        Globals.deltatime = 1/FPS



create_window()

player = Player("DefaultPlayer", 1)
player_w, player_h = player.width, player.height
player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size

man1 = Male1(name="Bob", pos=(200, 300))
man2 = Male1(name="Ted", pos=(400, 500))

def Play():
    Globals.scene = "game"

def Exit():
    global isRunning
    isRunning = False


# Initialize GUI
btnPlay = Menu.Button(text="Play", rect=(20, 20, 160, 60), bg=Color.Gray,
                      fg=Color.White, bgr=Color.CornflowerBlue, tag=("menu", None))
btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Command = Play
btnPlay.Top = (window_height /8) * 7

btnExit = Menu.Button(text="Exit", rect=(20, 20, 160, 60), bg=Color.Gray,
                      fg=Color.White, bgr=Color.CornflowerBlue, tag=("menu", None))
btnExit.Left = btnPlay.Left + btnPlay.Width + 3
btnExit.Top = (window_height /8) * 7
btnExit.Command = Exit

menuTitle = Menu.Text(text="PythonRPG", color=Color.Cyan, font=Font.Medium, tag=("menu", None))
menuTitle.Left, menuTitle.Top = 10, (window_height /8) * 7

logo = Menu.Image(bitmap=logo_img)

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command() # Do Button Event
                        btn.Rolling = False
                        break # Exit Loop

    # RENDER SCENE
    if Globals.scene == "game":

        # LOGIC
        if Globals.camera_move == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += 300 * Globals.deltatime
        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 300 * Globals.deltatime
        elif Globals.camera_move == 3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += 300 * Globals.deltatime
        elif Globals.camera_move == 4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 300 * Globals.deltatime

        player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
        player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size

        # RENDER GRAPHICS
        window.blit(Sky, (0, 0))

        window.blit(terrain, (Globals.camera_x, Globals.camera_y))

        for npc in NPC.AllNPCs:
            npc.Render(window)

        player.render(window, ((window_width / 2 - player_w / 2), (window_height / 2 - player_h / 2)))


    elif Globals.scene == "menu":

        logo.Render(window)

        for text in Menu.Text.All:
            if text.Tag[0] == "menu":
                text.Render(window)

        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(window)

    show_fps()

    pygame.display.update()

    clock.tick(60)
    count_fps()

pygame.quit()
sys.exit()
