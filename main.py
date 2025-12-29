import pygame
from logger import log_state, log_event
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, SCORE_PER_SMALL_ASTEROID, SCORE_PER_MEDIUM_ASTEROID, SCORE_PER_LARGE_ASTEROID
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    score = 0
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)
    
    font = pygame.font.Font(None, 36)  # None = default font, 36 = size

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for thing in updatable:
            thing.update(dt)

        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))  # position: top-left corner

        for thing in asteroids:
            if player1.collide_with(thing):
                log_event("player_hit")
                print("Game over!")
                print("Final score:", score)
                sys.exit()
            for shot in shots:
                if shot.collide_with(thing):
                    log_event("asteroid_shot")
                    thing.split()
                    if thing.radius <= ASTEROID_MIN_RADIUS:
                        score += SCORE_PER_SMALL_ASTEROID
                    elif thing.radius <= ASTEROID_MIN_RADIUS * 2:
                        score += SCORE_PER_MEDIUM_ASTEROID
                    else:
                        score += SCORE_PER_LARGE_ASTEROID
                    shot.kill()
            
        pygame.display.flip()
        dt = clock.tick(60)/1000.0  # Limit to 60 FPS
        
        log_state()
        
if __name__ == "__main__":
    main()
