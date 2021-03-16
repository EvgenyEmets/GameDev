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
MOVE = False
print(size)
s_x = 0
s_y = 0

bg = (0, 0, 255)

def check_resize(event):
    global size, scale_size, shift, RESIZE, width, height
    size = width, height = event.size
    scale_size = int(max(width, height) / 11)
    shift = int(min(width, height)/scale_size/2)
    RESIZE = True

map_size = 50

pos_x = random.randint(0, map_size)
pos_y = random.randint(0, map_size)

game_map = [[random.randint(0, 5) for i in range(map_size)] for j in range(map_size)]
print(pos_y)
#drow_map = [[pygame.Rect(i*50, j*50, 50, 50) for i in range(map_size)] for j in range(map_size)]
while True:
    if RESIZE:
        screen.fill(bg)
        for i in range(map_size):
            for j in range(map_size):
                color_val = game_map[i][j] * 50
                color = (color_val, color_val, color_val)
                pygame.draw.rect(screen, color, pygame.Rect(int((i-pos_x+5.5)*scale_size), int((j-pos_y+shift)*scale_size), scale_size, scale_size))
        pygame.display.flip()
        RESIZE = False
    if MOVE:
        for n in range(5):
            screen.fill(bg)
            pos_x = min(max(pos_x+s_x/5, 0), map_size)
            pos_y = min(max(pos_y+s_y/5, 0), map_size)
            for i in range(map_size):
                for j in range(map_size):
                    color_val = game_map[i][j] * 50
                    color = (color_val, color_val, color_val)
                    pygame.draw.rect(screen, color, pygame.Rect(int((i-pos_x+5.5)*scale_size), int((j-pos_y+shift)*scale_size), scale_size, scale_size))
            #pos_x = min(max(pos_x+s_x/5, 0), map_size)
            #pos_y = min(max(pos_y+s_y/5, 0), map_size)

            pygame.display.flip()
        MOVE = False
    for event in pygame.event.get():
        # EVENTS HANDLING
        # MOUSE EVENTS
        # KEYBOARD EVENTS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_s:
                #pos_y = min(pos_y+1, map_size)
                s_x = 0
                s_y = 1
            if event.key == pygame.K_a:
                #pos_x = max(pos_x-1, 0)
                s_x = -1
                s_y = 0
            if event.key == pygame.K_w:
                #pos_y = max(pos_y-1, 0)
                s_x = 0 
                s_y = -1
            if event.key == pygame.K_d:
                #pos_x = min(pos_x+1, map_size)
                s_x = 1
                s_y = 0
            MOVE = True

        # OTHER EVENTS
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.VIDEORESIZE:
            check_resize(event)
    
