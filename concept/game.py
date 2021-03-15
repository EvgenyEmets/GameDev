import time
import random
import pygame

pygame.init()
pygame.display.set_caption("Test Game")

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

info = pygame.display.Info()
size = width, height = info.current_w, info.current_h
print(size)

game_map = [[[0] for i in range(5)] for j in range(5)]
for i in range(5):
    for j in range(5):
        game_map[i][j] = random.randint(0, 5)
print(game_map)

pos_x = 0;
pos_y = 0;

drow_map = [[pygame.Rect(i*50, j*50, 50, 50) for i in range(5)] for j in range(5)]
for i in range(5):
    for j in range(5):
        color_val = game_map[i][j] * 50
        color = (color_val, color_val, color_val)
        pygame.draw.rect(screen, color, drow_map[i][j])
        pygame.display.flip()
time.sleep(1)
