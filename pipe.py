import pygame  # Import thư viện pygame để vẽ và di chuyển ống nước
import random  # Import random để tạo chiều cao ngẫu nhiên
from setting import WIDTH, HEIGHT, PIPE_SPEED  # Import các thông số từ setting.py

class Pipe:
    def __init__(self):
        """ Khởi tạo ống nước """
        self.image = pygame.transform.scale2x(pygame.image.load("assets/pipe-green.png"))  # Tải hình ảnh ống nước
        self.gap_size = 200  # Kích thước khoảng trống giữa ống nước trên và dưới
        self.pipe_list = []  # Danh sách chứa tất cả các ống nước hiện tại

    def create_pipe(self):
        """ Tạo một cặp ống nước trên và dưới """
        min_pipe_height = 200
        max_pipe_height = 500
        pipe_height = random.randint(min_pipe_height, max_pipe_height)

        bottom_pipe = {"rect": self.image.get_rect(midtop=(WIDTH, HEIGHT - pipe_height)), "passed": False}
        top_pipe = {"rect": self.image.get_rect(midbottom=(WIDTH, HEIGHT - pipe_height - self.gap_size)), "passed": False}

        return bottom_pipe, top_pipe  # Trả về cặp ống nước

    def move_pipes(self):
        """ Di chuyển ống nước sang trái và xóa nếu ra khỏi màn hình """
        for pipe in self.pipe_list:
            pipe["rect"].centerx -= PIPE_SPEED  # Di chuyển ống nước về bên trái

        # Xóa các ống nước đã ra khỏi màn hình
        self.pipe_list = [pipe for pipe in self.pipe_list if pipe["rect"].right > 0]

    def draw_pipes(self, screen):
        """ Vẽ ống nước lên màn hình """
        for pipe in self.pipe_list:
            if pipe["rect"].bottom > HEIGHT:
                screen.blit(self.image, pipe["rect"])  # Vẽ ống nước bình thường (dưới)
            else:
                flip_pipe = pygame.transform.flip(self.image, False, True)  # Lật ảnh cho ống trên
                screen.blit(flip_pipe, pipe["rect"])
