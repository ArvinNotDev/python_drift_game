from settings.settings import settings
import pygame
import sys  
from assets.cars import draw

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.general.screen_width, settings.general.screen_height))
        pygame.display.set_caption("Drift master")
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        pass  # update game logic

    def draw_map(self):
        self.screen.fill((30, 30, 30))

    def draw(self):
        self.draw_map()
        draw(self.screen, pygame.Vector2(400, 300))
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(settings.general.fps) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
