# Import the pygame library and initialize the game engine
import pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen
size = (800, 600)
screen = pygame.display.set_mode(size)

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)

# This is a rectangle that represents the ball
# It is drawn as a white circle with a radius of 20 pixels
ball = pygame.Rect(400, 300, 20, 20)

# This is a rectangle that represents the left paddle
# It is drawn as a white rectangle with a width of 20 pixels and a height of 100 pixels
left_paddle = pygame.Rect(50, 250, 20, 100)

# This is a rectangle that represents the right paddle
# It is drawn as a white rectangle with a width of 20 pixels and a height of 100 pixels
right_paddle = pygame.Rect(730, 250, 20, 100)

# This is the ball's movement vector. It moves 5 pixels
# to the right and 5 pixels down each frame, and will be
# multiplied by -1 (reversed) when it hits a wall or paddle
ball_vector = pygame.math.Vector2(5, 5)

# This is a counter that is used to control the ball's movement
# It counts down from 60 to 0, and when it reaches 0, the ball
# will change direction
counter = 60

# This is the game loop
while True:
    # Check for events
    for event in pygame.event.get():
        # If the event is the QUIT event, exit the game loop
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check if the ball has hit the left or right wall
    if ball.left <= 0 or ball.right >= 800:
        # Reverse the ball's x direction
        ball_vector.x *= -1

    # Check if the ball has hit the top or bottom wall
    if ball.top <= 0 or ball.bottom >= 600:
        # Reverse the ball's y direction
        ball_vector.y *= -1

    # Check if the ball has hit the left paddle
    if ball.colliderect(left_paddle):
        # Reverse the ball's x direction
        ball_vector.x *= -1

    # Check if the ball has hit the right paddle
    if ball.colliderect(right_paddle):
        # Reverse the ball's x direction
        ball_vector.x *= -1

    # Move the ball by its vector
    ball.move_ip(ball_vector)

    # If the counter is 0, change the ball's direction
    if counter == 0:
        # Reverse the ball's x and y directions
        ball_vector.x *= -1
        ball_vector.y *= -1

        # Reset the counter
        counter = 60

    # Decrement the counter
    counter -= 1

    # Clear the screen
    screen.fill(BLACK)

    # Draw
