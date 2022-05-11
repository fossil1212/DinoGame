import pygame, sys, time

def draw(obj, x, y):
    global screen
    screen.blit(obj, (x, y))


# initialization
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("dino game")
fps = pygame.time.Clock()

# object
tree = pygame.image.load("D:\프로그래밍\Python project\공룡게임\\tree.png")
tree_height = tree.get_size()[1]
tree_x = 800
tree_y = screen_height - tree_height

dino_1 = pygame.image.load("D:\프로그래밍\Python project\공룡게임\dino1.png")
dino_2 = pygame.image.load("D:\프로그래밍\Python project\공룡게임\dino2.png")
dino_size = dino_1.get_size()
dino_width = dino_size[0]
dino_height = dino_size[1]
dino_bottom = screen_height - dino_height
dino_top = 150
dino_x = 50
dino_y = dino_bottom
dino_to_y = 0
dino_legSwap = True
legTimer = 0

# main loop
running = True
dino_jumping = False
while running:

# event check
    for event in pygame.event.get():
        # game quit
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # key input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino_jumping:
                dino_jumping = True
                dino_to_y = -10



# dino 위치 조정
    dino_y += dino_to_y
    # 중력가속도
    dino_to_y += 0.5
    # 최대 높이보다 올라갔을 때 
    if dino_y <= dino_top:
        dino_y = dino_top
    # 바닥에 닿았을 때
    if dino_y >= dino_bottom:
        dino_y = dino_bottom
        dino_jumping = False
        dino_to_y = 0


# tree 위치 조정
    tree_x -= 10
    if tree_x == 0:
        tree_x = 800


# draw
    screen.fill((255, 255, 255))

    draw(tree, tree_x, tree_y)
    
    if dino_legSwap:
        draw(dino_1, dino_x, dino_y)
    else:
        draw(dino_2, dino_x, dino_y)

    legTimer += 1
    if legTimer%12 == 0:
        if dino_legSwap == True:
            dino_legSwap = False
        else:
            dino_legSwap = True


    pygame.display.update()


# Game over
    dino_rect = dino_1.get_rect()
    dino_rect.left = dino_x
    dino_rect.top = dino_y

    tree_rect = tree.get_rect()
    tree_rect.left = tree_x
    tree_rect.top = tree_y

    if dino_rect.colliderect(tree_rect):
        print("Game Over")
        running = False

    fps.tick(60)


