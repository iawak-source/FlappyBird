import pygame

# Kích thước màn hình
WIDTH, HEIGHT = 700, 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

# Tốc độ trọng lực
GRAVITY = 0.25

# Tốc độ di chuyển của ống nước
PIPE_SPEED = 5

# Thời gian xuất hiện ống nước
PIPE_SPAWN_TIME = 1600  # ms
