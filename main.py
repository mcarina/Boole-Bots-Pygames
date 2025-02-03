import pygame
import random

pygame.init()

WIDTH, HEIGHT = 300, 340
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boole Bots - Marcy's version")
clock = pygame.time.Clock()

class Bot:
    def __init__(self, x, y, value, operation):
        self.x = x
        self.y = y
        self.value = value  # 0 ou 1
        self.operation = operation  # AND, OR, NOT, etc.
        self.speed = random.randint(1, 3)
        self.color = (0, 255, 0) if self.value == 1 else (255, 0, 0)

    def move(self):
        self.x += random.choice([-self.speed, self.speed])
        self.y += random.choice([-self.speed, self.speed])
        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

# Criando bots aleatórios
bots = [Bot(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), 
            random.choice([0, 1]), random.choice(["AND", "OR", "NOT"])) for _ in range(5)]

# Loop do jogo
running = True
while running:
    screen.fill((30, 30, 30))
    
    for bot in bots:
        bot.move()
        bot.draw()
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()