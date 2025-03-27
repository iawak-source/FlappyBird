import pygame
from setting import WIDTH, HEIGHT

class Score:
    def __init__(self):
        """ Khởi tạo hệ thống điểm số """
        self.font = pygame.font.Font(None, 50)  # Font mặc định, kích thước 50px
        self.score = 0  # Điểm số hiện tại
        self.high_score = 0  # Điểm cao nhất đạt được

    # def update(self, pipes, bird):
    #     """ Cập nhật điểm khi chim vượt qua ống nước """
    #     for pipe in pipes:
    #         if pipe["rect"].right < bird.rect.left and not pipe.get("passed", False):
    #             pipe["passed"] = True  # Đánh dấu ống nước đã được vượt qua
    #             self.score += 0.5  # Cộng 1 điểm khi chim vượt qua ống nước
    def update(self, pipes, bird):
        for pipe in pipes:
            if pipe["rect"].right < bird.rect.left and not pipe.get("passed", False):
                if pipe["rect"].bottom > HEIGHT:
                    pipe["passed"] = True
                    self.score += 1

    def reset(self):
        """ Đặt lại điểm khi game kết thúc """
        self.high_score = max(self.high_score, self.score)  # Cập nhật điểm cao nhất
        self.score = 0  # Đặt lại điểm về 0 khi chơi lại

    def draw(self, screen):
        """ Hiển thị điểm số trên màn hình """
        # Tạo bề mặt hiển thị điểm số hiện tại
        score_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        # Tạo bề mặt hiển thị điểm cao nhất
        high_score_surface = self.font.render(f"High Score: {self.high_score}", True, (200, 200, 200))

        # Hiển thị điểm hiện tại ở vị trí trung tâm phía trên màn hình
        screen.blit(score_surface, (WIDTH // 2 - 50, 30))
        # Hiển thị điểm cao nhất ngay bên dưới điểm hiện tại
        screen.blit(high_score_surface, (WIDTH // 2 - 80, 70))
