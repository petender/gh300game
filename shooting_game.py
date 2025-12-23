import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
REACTION_TIME_LIMIT = 0.3

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Reflex Game")

# Fonts
font_large = pygame.font.Font(None, 74)
font_medium = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)


def get_player_name():
    """Get player name input from the user."""
    name = ""
    input_active = True
    
    while input_active:
        screen.fill(WHITE)
        
        # Draw prompt
        prompt_text = font_medium.render("Enter your name:", True, BLACK)
        screen.blit(prompt_text, (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, 200))
        
        # Draw current name
        name_text = font_small.render(name, True, BLUE)
        screen.blit(name_text, (SCREEN_WIDTH // 2 - name_text.get_width() // 2, 280))
        
        # Draw instruction
        instruction = font_small.render("Press ENTER to continue", True, BLACK)
        screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, 400))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isprintable():
                    name += event.unicode
    
    return name


def draw_shooter():
    """Draw the shooter at the bottom middle of the screen."""
    shooter_x = SCREEN_WIDTH // 2
    shooter_y = SCREEN_HEIGHT - 50
    
    # Draw simple triangle as shooter
    pygame.draw.polygon(screen, BLUE, [
        (shooter_x, shooter_y - 30),
        (shooter_x - 20, shooter_y + 10),
        (shooter_x + 20, shooter_y + 10)
    ])


def draw_target(x, y):
    """Draw the target at specified position."""
    pygame.draw.circle(screen, RED, (x, y), 30)
    pygame.draw.circle(screen, WHITE, (x, y), 20)
    pygame.draw.circle(screen, RED, (x, y), 10)


def play_game(player_name):
    """Main game logic."""
    clock = pygame.time.Clock()
    running = True
    game_state = "ready"  # ready, target_shown, result
    
    target_x = 0
    target_y = 0
    target_start_time = 0
    reaction_time = 0
    player_won = False
    
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == "target_shown":
                        # Calculate reaction time
                        reaction_time = time.time() - target_start_time
                        player_won = reaction_time < REACTION_TIME_LIMIT
                        game_state = "result"
                    elif game_state == "result":
                        # Start new round
                        game_state = "ready"
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        # Game state logic
        if game_state == "ready":
            # Show instruction and prepare to show target
            draw_shooter()
            instruction = font_small.render(f"Welcome {player_name}! Get ready...", True, BLACK)
            screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, 100))
            
            wait_text = font_small.render("Press SPACE when target appears!", True, BLACK)
            screen.blit(wait_text, (SCREEN_WIDTH // 2 - wait_text.get_width() // 2, 150))
            
            pygame.display.flip()
            
            # Wait a random time before showing target
            pygame.time.wait(random.randint(1000, 3000))
            
            # Generate random target position
            target_x = random.randint(100, SCREEN_WIDTH - 100)
            target_y = random.randint(100, SCREEN_HEIGHT - 150)
            target_start_time = time.time()
            game_state = "target_shown"
        
        elif game_state == "target_shown":
            draw_shooter()
            draw_target(target_x, target_y)
            
        elif game_state == "result":
            draw_shooter()
            
            # Show result
            if player_won:
                result_text = font_large.render("YOU WIN!", True, GREEN)
            else:
                result_text = font_large.render("YOU ARE TOO SLOW", True, RED)
            
            screen.blit(result_text, (SCREEN_WIDTH // 2 - result_text.get_width() // 2, 200))
            
            # Show reaction time
            time_text = font_medium.render(f"Time: {reaction_time:.3f}s", True, BLACK)
            screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, 300))
            
            # Show instruction for next round
            next_text = font_small.render("Press SPACE for next round or ESC to quit", True, BLACK)
            screen.blit(next_text, (SCREEN_WIDTH // 2 - next_text.get_width() // 2, 400))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


def main():
    """Main function to run the game."""
    player_name = get_player_name()
    if player_name:
        play_game(player_name)


if __name__ == "__main__":
    main()
