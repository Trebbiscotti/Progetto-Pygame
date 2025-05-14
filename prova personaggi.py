import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (100, 100, 255)

# Fonts
FONT = pygame.font.Font(None, 36)
TITLE_FONT = pygame.font.Font(None, 48)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Character Selection")

# Character options
characters = ["Character 1", "Character 2", "Character 3"]
character_rects = []

# Positions for character options
spacing = 200
start_x = (SCREEN_WIDTH - (spacing * (len(characters) - 1) + 100)) // 2
start_y = (SCREEN_HEIGHT - 200) // 2

# Load images
character_image = pygame.image.load("cavaliere.jpg")
character_image = pygame.transform.scale(character_image, (100, 100))
sfondo_image = pygame.image.load("sfondo.jpg")
sfondo_image = pygame.transform.scale(sfondo_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Main loop
selected_character = None
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, rect in enumerate(character_rects):
                if rect.collidepoint(mouse_pos):
                    selected_character = characters[i]

                    # Change to new screen
                    adventure_running = True
                    message = "Che l'avventura cominci"
                    char_x = 50
                    char_y = SCREEN_HEIGHT - 150  # Position character at bottom left
                    text_surface = FONT.render("", True, BLACK)
                    text_rect = pygame.Rect(150, SCREEN_HEIGHT - 120, SCREEN_WIDTH - 300, 60)  # Message box
                    index = 0

                    # Display message one character at a time
                    while adventure_running:
                        screen.blit(sfondo_image, (0, 0))

                        # Draw selected character in the bottom left
                        screen.blit(character_image, (char_x, char_y))

                        # Draw message box (white with black border)
                        pygame.draw.rect(screen, WHITE, text_rect)
                        pygame.draw.rect(screen, BLACK, text_rect, 2)

                        # Show full message after it's completed
                        if index < len(message):
                            text_surface = FONT.render(message[:index], True, BLACK)
                            index += 1
                        else:
                            # Once the full message is displayed, stop updating it
                            text_surface = FONT.render(message, True, BLACK)

                        # Draw the message inside the box
                        screen.blit(text_surface, text_rect)

                        # Event handling for the new screen
                        for adv_event in pygame.event.get():
                            if adv_event.type == pygame.QUIT:
                                adventure_running = False
                                running = False

                        pygame.display.flip()
                        time.sleep(0.05)  # Adjust speed here

                    # Once the message is fully shown, proceed with next steps or end the game
                    time.sleep(1)  # Pause for 1 second before ending

    # Draw title
    title_surface = TITLE_FONT.render("Choose Your Character", True, BLACK)
    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(title_surface, title_rect)

    # Draw character options
    character_rects = []
    for i, name in enumerate(characters):
        x = start_x + i * spacing
        y = start_y
        rect = pygame.Rect(x, y, 100, 100)
        character_rects.append(rect)

        # Highlight on hover
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, HIGHLIGHT, rect)
        else:
            pygame.draw.rect(screen, BLACK, rect, 2)

        # Draw the image and name
        screen.blit(character_image, (x, y))
        text_surface = FONT.render(name, True, BLACK)
        text_rect = text_surface.get_rect(center=(x + 50, y + 120))
        screen.blit(text_surface, text_rect)

    # Draw instruction text
    instruction_surface = FONT.render("Select your character", True, BLACK)
    instruction_rect = instruction_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
    screen.blit(instruction_surface, instruction_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
