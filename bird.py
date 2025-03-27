import pygame
from setting import HEIGHT  # Import chiều cao của màn hình từ setting.py

class Bird:
    def __init__(self):
        """Khởi tạo chim và các thuộc tính ban đầu"""
        # Tạo danh sách các hình ảnh của chim trong 3 trạng thái vỗ cánh
        self.frames = [
            pygame.transform.scale(pygame.image.load("assets/yellowbird-downflap.png"), (51, 36)),
            pygame.transform.scale(pygame.image.load("assets/yellowbird-midflap.png"), (51, 36)),
            pygame.transform.scale(pygame.image.load("assets/yellowbird-upflap.png"), (51, 36))
        ]
        self.index = 0  # Chỉ số của hình ảnh chim trong danh sách
        self.image = self.frames[self.index]  # Chọn hình ảnh chim ban đầu
        self.rect = self.image.get_rect(center=(100, HEIGHT//2))  # Đặt vị trí ban đầu của chim ở giữa màn hình
        self.movement = 0  # Vận tốc ban đầu của chim

    def flap(self):
        """Khi người chơi nhấn phím, chim sẽ bay lên"""
        self.movement = -6  # Cập nhật vận tốc của chim (bay lên)

    def update(self, gravity):
        """Cập nhật vận tốc và vị trí chim mỗi khung hình"""
        self.movement += gravity  # Thêm trọng lực vào vận tốc của chim
        self.rect.centery += self.movement  # Cập nhật vị trí của chim theo vận tốc

    def animate(self):
        """Cập nhật hình ảnh chim để tạo hiệu ứng vỗ cánh"""
        self.index = (self.index + 1) % len(self.frames)  # Chuyển sang hình ảnh tiếp theo
        self.image = self.frames[self.index]  # Cập nhật hình ảnh của chim

    def rotate(self):
        """Tính toán góc quay của chim dựa trên vận tốc"""
        angle = min(max(-self.movement * 3, -30), 90)  # Giới hạn góc quay từ -30 đến 90 độ, góc âm chim bay lên, góc dương chim bay xuống
        return pygame.transform.rotate(self.image, angle)  # Xoay chim theo góc đã tính toán

    def draw(self, screen):
        """Vẽ chim lên màn hình"""
        screen.blit(self.rotate(), self.rect)  # Vẽ chim đã được xoay tại vị trí của nó

    def reset(self):
        """Đặt lại chim về vị trí ban đầu khi game kết thúc hoặc bắt đầu lại"""
        self.rect.center = (100, HEIGHT//2)  # Đặt chim về vị trí giữa màn hình
        self.movement = 0  # Đặt vận tốc chim về 0
