import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from fps_counter import FPSCounter
from menu import Menu
from scoreboard import Scoreboard
from background import Background


def run_game():
    # Init the game and create window object
    pygame.init()
    ai_settings = Settings()
    clock = pygame.time.Clock()


    screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)

    #background = pygame.images.load('background.jpg') - need help with my backgrounds screan not working at all
    pygame.display.set_caption("Alien Invasion")

    # Create an instance for game statistics storage & scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    fps_counter = FPSCounter(ai_settings, screen)

    # Create menu
    menu = Menu(screen, stats)

    # Create the ship, bullets group & aliens group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()

    # Create aliens fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Ticks
    ticks = 0

    game_process = True

    # Start main game loop
    while game_process:
        fps = int(clock.get_fps())

        gf.check_events(
            ai_settings, screen, stats, sb, menu, ship, aliens, bullets)

        if stats.game_active:
            ticks += 1
            ship.update()
            gf.update_bullets(
                ai_settings, screen, stats, sb, ship,
                aliens, bullets, alien_bullets)

            gf.update_aliens(
                ai_settings, stats, sb, screen, ship,
                aliens, bullets, alien_bullets, ticks)

            if ticks % ai_settings.tick_factor == 0:
                ticks = 0

        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens,
            bullets, alien_bullets, menu, fps_counter, fps)

        clock.tick(ai_settings.fps)


run_game()
