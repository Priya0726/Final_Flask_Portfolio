import pygame
import sys
import time

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

BLUE = (137, 207, 245)
GREEN = (108, 118, 91)

clock = pygame.time.Clock()

running = True
start_time = time.time()

while running:
    screen.fill(BLUE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, GREEN, (0.5, HEIGHT * 0.8, WIDTH, HEIGHT * 0.4))

    elapsed_time = time.time() - start_time
    if elapsed_time >= 30:
        print("Time's up! Game paused.")
        print("Resume after 30 seconds...")
        time.sleep(30)
        
        start_time = time.time()
        print("Game resumed!")


    pygame.display.flip()

    clock.tick(30)
clock = pygame.time.Clock()

# Track whether the question screen is active
question_screen_active = False

# Function to display the question screen
def display_question_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    question_text = font.render("What is the capital of France?", True, BLACK)
    screen.blit(question_text, (50, 50))

    # Display multiple-choice options
    option_a = font.render("A) London", True, BLACK)
    screen.blit(option_a, (50, 150))

    option_b = font.render("B) Paris", True, BLACK)
    screen.blit(option_b, (50, 200))

    option_c = font.render("C) Rome", True, BLACK)
    screen.blit(option_c, (50, 250))


pygame.quit()
sys.exit()
