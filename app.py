import pygame, sys, math, random, time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
circle_pos = (1280/2, 720/2)
font = pygame.font.Font(None, 30)
score = 0

SMALL_RADIUS_MIN, SMALL_RADIUS_MAX = 10, 40  
MEDIUM_RADIUS_MIN, MEDIUM_RADIUS_MAX = 41, 60  
circle_radius = 50  

reaction_time = 0
circle_appear_time = time.time()

def check_circle_condition() -> bool:
    mouse_pos = pygame.mouse.get_pos()
    return math.hypot(mouse_pos[0] - circle_pos[0], mouse_pos[1] - circle_pos[1]) <= circle_radius

def spawn_new_circle():
    global circle_pos, circle_radius, circle_appear_time
    circle_pos = (random.randint(0, 1280), random.randint(0, 720))
    if random.choice([True, False]):
        circle_radius = random.randint(SMALL_RADIUS_MIN, SMALL_RADIUS_MAX)
    else:
        circle_radius = random.randint(MEDIUM_RADIUS_MIN, MEDIUM_RADIUS_MAX)
    circle_appear_time = time.time()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if check_circle_condition():
                    reaction_time = time.time() - circle_appear_time
                    print(f"Reaction Time: {int(reaction_time * 1000)} ms")
                    score += 1
                    spawn_new_circle()
                else:
                    score -= 1

    screen.fill('lightblue')
    pygame.draw.circle(screen, 'red', circle_pos, circle_radius)
    
    score_text = font.render(f'Score: {score}', True, 'black')
    reaction_text = font.render(f'Reaction Time: {int(reaction_time * 1000)} ms', True, 'black')
    
    screen.blit(score_text, (50, 50))
    screen.blit(reaction_text, (50, 90))
    
    pygame.display.update()
