import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with blue color
    screen.fill("blue")

    # Draw the red circle (player)
    pygame.draw.circle(screen, "red", player_pos, 40)

    # Get the pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Update the display
    pygame.display.flip()

    # Frame time control
    dt = clock.tick(60) / 1000

pygame.quit()


# THIS COMMENT IS JUST TO SHOW I KNOW HOW TO COMMIT TO AN EXISTING REPO