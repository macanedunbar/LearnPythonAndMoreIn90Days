import pygame

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