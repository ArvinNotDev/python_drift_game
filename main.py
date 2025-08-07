from settings.settings import settings as Settings
import pygame
import sys  

settings = Settings()

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
            # events are here
    
    def update(self, dt):
        # updating game objects
        pass

    def draw_map(self):
        self.screen.fill((30, 30, 30))

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(settings.general.fps) / 1000  # Delta time in seconds so more fps doesn't bother the gameplay
            self.handle_events()
            self.draw()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()