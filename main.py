import pygame ,sys ,random

def ball_animation():
    #updating objectd varibale values-like speed/position etc.
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x 
    ball.y += ball_speed_y 
    
    #checking for ball collisions with 4-sides
    if ball.top <= 0  or ball.bottom >= HEIGHT:
        ball_speed_y *= -1 
    if ball.left <= 0 or ball.right >= WIDTH:
        game_restart()
    #collsion between ball and paddle
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1    
        

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
    
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

def game_restart():
    global ball_speed_x, ball_speed_y
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))
    ball.center = (WIDTH/2, HEIGHT/2)



pygame.init()

WIDTH = 800
HEIGHT = 610
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')
clock = pygame.time.Clock()

#game objects 
ball = pygame.Rect(WIDTH/2-15, HEIGHT/2-15, 30, 30)
player = pygame.Rect(WIDTH - 20 ,HEIGHT/2-70 ,10, 140)
opponent = pygame.Rect(10 ,HEIGHT/2-70 ,10, 140)

#color variables
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

# Adjusting objects speed 
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0 
opponent_speed = 10

while True:
    #checking all events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            # player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    
    ball_animation()
    player_animation()
    opponent_ai()

    
    
    #displaying all objects on screen
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (WIDTH/2,0),(WIDTH/2, HEIGHT))
    
    #updating the window
    pygame.display.flip()
    clock.tick(60)