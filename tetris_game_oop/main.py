import pygame,sys
from grid_for_tetris import Grid
from individual_blocks import LBlock

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

blocks_for_tetris = LBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        screen.fill(dark_blue)
        game_grid.draw(screen)
        blocks_for_tetris.draw(screen)

        pygame.display.update()
        clock.tick(60)