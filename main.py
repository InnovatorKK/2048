import pygame
import random
from sys import exit
from tile import Tile


def main():
     
    pygame.init()
    screen = pygame.display.set_mode((650, 650))
    clock = pygame.time.Clock()

    pygame.display.set_caption("2048")
    
    screen.fill('Yellow')
    
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(25, 25, 600, 600))

    
    tilekSize = 150 #Set the size of the grid block
    for x in range(0, 600, tilekSize):
        for y in range(0, 600, tilekSize):
            rect = pygame.Rect(x+25, y+25, tilekSize, tilekSize)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
    
    tile = Tile(2, 0, 0)
    tileList = [[0 for i in range(4)] for _ in range(4)]
    print(tileList)
    
    tiles = pygame.sprite.Group()
    tiles.add(tile)
    while True:
        
        # tile.update()
        tiles.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tile = Tile(random.randint(1, 5), random.randint(0, 3), random.randint(0, 3))
                    tiles.add(tile)
                    print("DOWN")
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                


if __name__=="__main__":
    main()