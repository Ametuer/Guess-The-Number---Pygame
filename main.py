import pygame, random

pygame.init()

# Game setup
screen = pygame.display.set_mode((600, 600))  # Set screen dimensions
pygame.display.set_caption('Testing')  # Set window title
clock = pygame.time.Clock()  # Initialize game clock
font = pygame.font.SysFont('Comic Sans MS', 50)  # Initialize font

# Game variables
running = True
guess = random.randint(1, 100)
input_text = ""
win_state = "Guess the number! From 1-100"

def game_logic(n):
    """
    Determine the result of the guess based on the input number.

    Parameters:
        n (int): The guessed number.

    Returns:
        str: The result message.
    """
    return "You Win!" if n == guess else ("Too Low!" if n < guess else "Too High!")  # Check the guess result

# Main game loop
while running:
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Render text
    screen.blit(font.render(win_state, True, (0, 0, 0)), (50, 100))  # Render win state text
    screen.blit(font.render(input_text, True, (0, 0, 0)), (50, 200))  # Render input text
    pygame.display.update()  # Update the display

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exit the game loop
            running = False
            break
        if event.type == pygame.KEYDOWN:  # Check if a key is pressed
            if event.key == pygame.K_BACKSPACE:  # Remove the last character from input text
                input_text = input_text[:-1]
            elif event.key == pygame.K_r: # Reset the game variables
                guess = random.randint(1, 100)
                win_state = "Guess the number! From 1-100""
                input_text = "" 
            elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER] and input_text != "":  # Check if Enter is pressed and input is not empty
                win_state = game_logic(int(input_text)) 
                input_text = ""
            elif event.unicode.isdigit():  # Add the digit to the input text
                input_text += event.unicode 

    clock.tick(30)  # Limit the frame rate

pygame.quit()  # Quit pygame
