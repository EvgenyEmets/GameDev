import time
import random
import pygame

pygame.init()
pygame.display.set_caption("Test Game")

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

info = pygame.display.Info()
size = width, height = info.current_w, info.current_h
scale_size = int(max(width, height) / 11)
print(scale_size)
shift = int(min(width, height)/scale_size/2)
RESIZE = True
print(size)

bg = (0, 0, 255)

def check_resize(event):
    global size, scale_size, shift, RESIZE, width, height
    size = width, height = event.size
    scale_size = int(max(width, height) / 11)
    shift = int(min(width, height)/scale_size/2)
    RESIZE = True
    print("!!!!!!!!")

map_size = 50

pos_x = 0 #random.randint(0, map_size)
pos_y = 0 #random.randint(0, map_size)
game_map = [[random.randint(0, 5) for i in range(map_size)] for j in range(map_size)]
print(game_map)
#drow_map = [[pygame.Rect(i*50, j*50, 50, 50) for i in range(map_size)] for j in range(map_size)]
while True:
    if RESIZE:
        screen.fill(bg)
        print(scale_size)
        for i in range(map_size):
            for j in range(map_size):
                color_val = game_map[i][j] * 50
                color = (color_val, color_val, color_val)
                pygame.draw.rect(screen, color, pygame.Rect((i-pos_x+5)*scale_size, (j-pos_y+shift)*scale_size, scale_size, scale_size))
        pygame.display.flip()
        RESIZE = False
    for event in pygame.event.get():
        # EVENTS HANDLING
        # MOUSE EVENTS
        # KEYBOARD EVENTS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        # OTHER EVENTS
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.VIDEORESIZE:
            check_resize(event)
    
