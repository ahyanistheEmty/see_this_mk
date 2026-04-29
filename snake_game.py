import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# --- Game Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0) # Changed from GREEN to ORANGE
RED = (255, 0, 0)
BLUE = (50, 153, 213) # Background color

# Snake properties
SNAKE_SPEED = 10 # Frames per second

# --- Set up the display ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Classic Snake Game")
clock = pygame.time.Clock()

# --- Font settings ---
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    """Displays the current score on the screen."""
    value = score_font.render("Your Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    """Draws the snake on the screen."""
    # The snake is now drawn in ORANGE color
    for x in snake_list:
        pygame.draw.rect(screen, ORANGE, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Displays a message on the screen."""
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(mesg, text_rect)

def game_loop():
    """Main game loop for the Snake game."""
    game_over = False
    game_close = False

    # Initial snake position and movement
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Generate initial food position
    foodx = round(random.randrange(0, SCREEN_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
    foody = round(random.randrange(0, SCREEN_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE

    while not game_over:
        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop() # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change == GRID_SIZE: # Prevent 180-degree turn
                        continue
                    x1_change = -GRID_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change == -GRID_SIZE: # Prevent 180-degree turn
                        continue
                    x1_change = GRID_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change == GRID_SIZE: # Prevent 180-degree turn
                        continue
                    y1_change = -GRID_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change == -GRID_SIZE: # Prevent 180-degree turn
                        continue
                    y1_change = GRID_SIZE
                    x1_change = 0

        # Check for boundary collision
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)

        # Draw food
        pygame.draw.rect(screen, RED, [foodx, foody, GRID_SIZE, GRID_SIZE])

        # Update snake body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Limit snake length
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for self-collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw snake
        draw_snake(GRID_SIZE, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check for food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
            foody = round(random.randrange(0, SCREEN_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
