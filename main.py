import pygame
import sys
from assets.cars import normal_car
from settings.settings import settings
from movements import keyboard_moves_car



class Camera:
    def __init__(self, screen_width, screen_height):
        self.offset = pygame.Vector2(0, 0)
        self.screen_center = pygame.Vector2(screen_width // 2, screen_height // 2)

    def follow(self, target_pos: pygame.Vector2):
        self.offset = target_pos - self.screen_center


class Game:
    def __init__(self):
        self.settings = settings
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.general.screen_width, self.settings.general.screen_height))
        pygame.display.set_caption("Drift Master")
        self.clock = pygame.time.Clock()
        self.running = True
        self.car_pos = pygame.Vector2(1000, 1000)
        self.car_angle = 0
        self.camera = Camera(self.settings.general.screen_width, self.settings.general.screen_height)
        self.velocity = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        self.car_angle, self.velocity = keyboard_moves_car(self.car_angle, self.car_pos, dt, self.settings.physics.speed, self.settings.drift.steering_speed,
                                                           self.settings.physics.max_speed, self.settings.physics.acceleration, self.settings.physics.deceleration, 
                                                           self.settings.physics.reverse_speed, self.velocity)
        self.camera.follow(self.car_pos)
        


    def draw_map(self):
        self.screen.fill((30, 30, 30))

        # simple world ground
        tile_size = 100
        world_width = 3000
        world_height = 3000

        for x in range(0, world_width, tile_size):
            for y in range(0, world_height, tile_size):
                world_tile_pos = pygame.Vector2(x, y)
                screen_tile_pos = world_tile_pos - self.camera.offset
                rect = pygame.Rect(screen_tile_pos.x, screen_tile_pos.y, tile_size, tile_size)
                pygame.draw.rect(self.screen, (50, 50, 50), rect, 1)

    def draw(self):
        self.draw_map()

        screen_pos = self.car_pos - self.camera.offset
        normal_car(self.screen, screen_pos, self.car_angle)

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(self.settings.general.fps) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
