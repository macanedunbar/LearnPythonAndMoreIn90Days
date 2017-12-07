import pygame
import math
import sys
from PythonRPG.Scripts.UltraColor import *
from PythonRPG.Scripts.textures import *

def export_map(file):
    map_data = ""
    #Get Map Dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    #Save Map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / Tiles.Size)) \
                   + "," + str(int(tile[1] / Tiles.Size)) + ":" + tile[2] + "-"

    #Save Map Dimensions
    map_data = map_data + str(int(max_x / Tiles.Size)) + "," \
               + str(int(max_y / Tiles.Size))

    #Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)


window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * Tiles.Size, 100 * Tiles.Size

selector = pygame.Surface((Tiles.Size, Tiles.Size), pygame.HWSURFACE | pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.CornflowerBlue))

tile_data = []

camera_x, camera_y, camera_move = 0, 0, 0

brush = "1"

# Initialize Default Terrain
for x in range(0, map_width, Tiles.Size):
    for y in range(0, map_height, Tiles.Size):
        tile_data.append([x, y, "1"])

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4
        elif event.type == pygame.KEYUP:
            camera_move = 0

        # Brushes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4:
                brush = "r"
            elif event.key == pygame.K_F3:
                brush = "3"
            elif event.key == pygame.K_F2:
                brush = "2"
            elif event.key == pygame.K_F1:
                brush = "1"
            elif event.key == pygame.K_F5:
                selection = input("Brush Tag: ")
                brush = selection

            #Save Map
            elif event.key == pygame.K_F12:
                mapname = input("Map Name:")
                export_map(mapname + ".map")
                print(mapname + ".map Saved Successfully")

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / Tiles.Size) * Tiles.Size
            mouse_y = math.floor(mouse_pos[1] / Tiles.Size) * Tiles.Size

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush] #Keep this as a list

            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1]:
                    found = True
                    tile_data.remove(t)
                    print("Tile @", t[0], ",", t[1], "removed")
                    tile_data.append(tile)
                    print("Tile Type", brush, "@", t[0], ",", t[1], "appended")
                    break

            if not found:
                if not brush == "r":
                    tile_data.append(tile)

    # LOGIC
    if camera_move == 1:
        camera_y += Tiles.Size
    elif camera_move == 2:
        camera_y -= Tiles.Size
    elif camera_move == 3:
        camera_x += Tiles.Size
    elif camera_move == 4:
        camera_x -= Tiles.Size
    window.fill(Color.Black)

    # Draw Map
    for tile in tile_data:
        try:
            window.blit(Tiles.Texture_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    # Draw Tile Highlighter
    window.blit(selector, (mouse_x, mouse_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
