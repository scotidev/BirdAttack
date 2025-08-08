import pygame
import sys
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_RED


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/GameOverBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/GameOver.wav')
        pygame.mixer_music.play()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.game_over_text(70, "GAME OVER", C_RED, (WIN_WIDTH / 2, 100))
            self.game_over_text(25, "Pressione 'ENTER'", C_RED, (WIN_WIDTH / 2, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            pygame.display.flip()

    def game_over_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)