import pygame  # Thư viện pygame để xử lý đồ họa
import sys  # Để thoát trò chơi khi đóng cửa sổ
from setting import screen, clock, GRAVITY, PIPE_SPAWN_TIME  # Thông số từ file setting.py
from bird import Bird  # Lớp chim
from pipe import Pipe  # Lớp ống nước
from floor import Floor  # Lớp mặt đất
from score import Score  # Lớp điểm số

class Game:
    def __init__(self):
        pygame.init()  # Khởi tạo các mô-đun của Pygame
        self.bg = pygame.transform.scale(pygame.image.load("assets/background-night.png"), (700, 900))  # Tải và thay đổi kích thước hình nền
        self.bird = Bird()  # Khởi tạo đối tượng chim
        self.pipes = Pipe()  # Khởi tạo đối tượng ống nước
        self.floor = Floor()  # Khởi tạo đối tượng mặt đất
        self.score = Score()  # Khởi tạo đối tượng điểm số
        self.game_state = "menu"  # Trạng thái ban đầu của trò chơi là "menu"
        self.game_over_surface = pygame.image.load("assets/gameover.png")  # Tải hình ảnh game over
        self.game_over_rect = self.game_over_surface.get_rect(center=(350, 450))  # Đặt hình ảnh game over vào trung tâm

        # Thiết lập các sự kiện định kỳ
        pygame.time.set_timer(pygame.USEREVENT + 1, 200)  # Chim vỗ cánh mỗi 200ms
        pygame.time.set_timer(pygame.USEREVENT, PIPE_SPAWN_TIME)  # Tạo ống nước mới mỗi PIPE_SPAWN_TIME

    def reset_game(self):
        """ Đặt lại trò chơi khi kết thúc hoặc người chơi muốn chơi lại """
        self.bird.reset()  # Đặt lại chim về vị trí ban đầu
        self.pipes.pipe_list.clear()  # Xóa tất cả các ống nước
        self.score.reset()  # Đặt lại điểm số
        self.game_state = "menu"  # Đặt lại trạng thái trò chơi về "menu"

    def check_collision(self):
        """ Kiểm tra va chạm giữa chim và ống nước, hoặc chim ra ngoài màn hình """
        for pipe in self.pipes.pipe_list:
            if self.bird.rect.colliderect(pipe["rect"]):  # Kiểm tra va chạm giữa chim và ống nước
                return False
        if self.bird.rect.top <= -50 or self.bird.rect.bottom >= 800:  # Kiểm tra nếu chim ra ngoài màn hình
            return False
        return True  # Nếu không va chạm, trò chơi tiếp tục

    def run(self):
        """ Vòng lặp chính của trò chơi """
        while True:
            for event in pygame.event.get():  # Lấy tất cả sự kiện từ người chơi
                if event.type == pygame.QUIT:  # Nếu người chơi đóng cửa sổ game
                    pygame.quit()
                    sys.exit()

                # Kiểm tra sự kiện nhấn phím
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.game_state == "menu":
                        self.game_state = "play"  # Chuyển sang chế độ chơi
                    elif self.game_state == "play":
                        self.bird.flap()  # Làm chim bay lên
                    elif self.game_state == "game_over":
                        self.reset_game()  # Bắt đầu lại trò chơi

                # Kiểm tra sự kiện click chuột
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_state == "menu":
                        self.game_state = "play"
                    elif self.game_state == "play":
                        self.bird.flap()
                    elif self.game_state == "game_over":
                        self.reset_game()

                # Tạo ống nước mới
                if event.type == pygame.USEREVENT and self.game_state == "play":
                    self.pipes.pipe_list.extend(self.pipes.create_pipe())

                # Thay đổi hình ảnh chim để tạo hiệu ứng vỗ cánh
                if event.type == pygame.USEREVENT + 1:
                    self.bird.animate()

            # Vẽ nền
            screen.blit(self.bg, (0, 0))

            # Trạng thái menu
            if self.game_state == "menu":
                message_surface = pygame.image.load("assets/message.png")
                message_surface = pygame.transform.scale2x(message_surface)  # Phóng to thông điệp
                message_rect = message_surface.get_rect(center=(350, 450))  # Đặt vị trí thông điệp
                screen.blit(message_surface, message_rect)  # Vẽ thông điệp lên màn hình

            # Trạng thái chơi
            elif self.game_state == "play":
                self.bird.update(GRAVITY)  # Cập nhật vị trí và vận tốc của chim
                self.pipes.move_pipes()  # Di chuyển ống nước
                self.game_state = "game_over" if not self.check_collision() else "play"  # Kiểm tra va chạm

                # Vẽ ống nước và chim lên màn hình
                self.pipes.draw_pipes(screen)
                self.bird.draw(screen)

                # Cập nhật và vẽ điểm số
                self.score.update(self.pipes.pipe_list, self.bird)  
                self.score.draw(screen)

            # Trạng thái game over
            elif self.game_state == "game_over":
                screen.blit(self.game_over_surface, self.game_over_rect)  # Vẽ hình game over lên màn hình

            # Di chuyển và vẽ mặt đất lên màn hình
            self.floor.move()
            self.floor.draw(screen)

            pygame.display.update()  # Cập nhật màn hình
            clock.tick(80)  # Điều chỉnh tốc độ khung hình (FPS)
