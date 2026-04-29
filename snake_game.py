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
ORANGE = (255, 165, 0) # Snake color
RED = (255, 0, 0)
BLUE = (50, 153, 213) # Background color

# Snake properties
# SNAKE_SPEED_FACTOR now affects how quickly the snake's velocity matches the target direction
SNAKE_SPEED_FACTOR = 0.2 # How much velocity tries to match target direction per frame (0 to 1)
# INITIAL_SNAKE_SPEED = 5 # Base speed of the snake - this is no longer directly used for movement step

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

    # Initial snake position
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    # Physics-based movement variables
    dx = 0 # Current horizontal velocity
    dy = 0 # Current vertical velocity
    target_dx = 0 # Desired horizontal direction
    target_dy = 0 # Desired vertical direction

    snake_list = []
    length_of_snake = 1

    # Generate initial food position
    foodx = round(random.randrange(0, SCREEN_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
    foody = round(random.randrange(0, SCREEN_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE

    # --- Game Timer ---
    # We'll use the timer to control movement steps rather than clock.tick directly
    # This allows for more consistent movement regardless of frame rate fluctuations.
    MOVE_INTERVAL = 100 # milliseconds between snake movements
    last_move_time = pygame.time.get_ticks()

    while not game_over:
        current_time = pygame.time.get_ticks()

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
                # Set target direction, but prevent immediate 180 turns
                if event.key == pygame.K_LEFT:
                    if target_dx != GRID_SIZE: # If not already moving right
                        target_dx = -GRID_SIZE
                        target_dy = 0
                elif event.key == pygame.K_RIGHT:
                    if target_dx != -GRID_SIZE: # If not already moving left
                        target_dx = GRID_SIZE
                        target_dy = 0
                elif event.key == pygame.K_UP:
                    if target_dy != GRID_SIZE: # If not already moving down
                        target_dy = -GRID_SIZE
                        target_dx = 0
                elif event.key == pygame.K_DOWN:
                    if target_dy != -GRID_SIZE: # If not already moving up
                        target_dy = GRID_SIZE
                        target_dx = 0

        # --- Physics Simulation for Movement ---
        # Gradually move current velocity towards target direction
        dx += (target_dx - dx) * SNAKE_SPEED_FACTOR
        dy += (target_dy - dy) * SNAKE_SPEED_FACTOR

        # Apply velocity, scaled by time elapsed and a base speed
        # We round to nearest GRID_SIZE to keep it on the grid, but the dx/dy are continuous
        # This provides a smoother movement.
        elapsed_time_ms = current_time - last_move_time
        if elapsed_time_ms >= MOVE_INTERVAL:
            x1 += dx * (MOVE_INTERVAL / 1000) # Scale movement by time
            y1 += dy * (MOVE_INTERVAL / 1000)

            # Snap to grid position for collision and drawing consistency
            # This ensures the snake segments align properly
            x1 = round(x1 / GRID_SIZE) * GRID_SIZE
            y1 = round(y1 / GRID_SIZE) * GRID_SIZE
            
            last_move_time = current_time # Reset timer

            # Check for boundary collision
            if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
                game_close = True

            # Update snake body
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)

            # Limit snake length
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Check for self-collision
            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True
                    break # Exit loop early if collision detected

            # --- Drawing and Display Update ---
            screen.fill(BLUE)
            # Draw food
            pygame.draw.rect(screen, RED, [foodx, foody, GRID_SIZE, GRID_SIZE])
            # Draw snake
            draw_snake(GRID_SIZE, snake_list)
            display_score(length_of_snake - 1)
            pygame.display.update()

            # Check for food collision
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, SCREEN_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
                foody = round(random.randrange(0, SCREEN_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
                length_of_snake += 1

        # Control frame rate - this is now more for rendering smoothness than movement speed
        clock.tick(60) # Aim for 60 frames per second for rendering

    pygame.quit()
    quit()

game_loop()
