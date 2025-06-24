# Import necessary modules
import pygame,sys
from game import Game
from colors_for_tetris import Colors

# Initialize Pygame
pygame.init()

# Create font and render UI text surfaces
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Define rectangles for Score and Next sections
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Set up the main game window
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

game = Game()

# Set a custom event for automatic piece movement
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Main game loop
while True:
    for event in pygame.event.get():
        # Handle window close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
        # Handle key presses for game controls
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
                game.game_over = False
            elif not game.game_over:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()

        # Automatically move piece down at regular interval
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Clear the screen with background color
    screen.fill(Colors.dark_blue)

    # Draw UI text headers
    screen.blit(score_surface, (365, 20))
    screen.blit(next_surface, (375, 180))

    # Draw game over message if applicable
    if game.game_over:
        screen.blit(game_over_surface, (320, 450))

    # Draw the Score and Next rectangles
    pygame.draw.rect(screen, Colors.light_blue, score_rect, border_radius=10)
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.blit(score_value_surface, score_value_surface.get_rect(center=score_rect.center))

    pygame.draw.rect(screen, Colors.light_blue, next_rect, border_radius=10)

    game.draw(screen)

    # Update the display
    pygame.display.update()

    # Cap the frame rate to 60 FPS
    clock.tick(60)