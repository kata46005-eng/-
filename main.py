import pygame


pygame.init()

class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color = (255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def filling(self):
        pygame.draw.rect(wn, self.fill_color, self.rect)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, image, x = 0, y = 0, width = 10, height = 10, color = (255, 255, 255)):
        super().__init__(x , y , width , height , color)
        self.image = pygame.image.load(image)

    def draw(self, shift_x = 0, shift_y = 0):
        self.filling()
        wn.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) 


scene = (143, 182, 233)
wn = pygame.display.set_mode(500, 500)
wn.fill(scene)
clock = pygame.time.Clock()

ball = Picture('ball.png', 200, 200, 50, 50, scene)
ball.draw()

platform = Picture('platform.png', 300, 350, 100, 30, scene)
platform.draw()

monsters = list()
n = 9
start_x = 5
start_y = 5
for j in range(3):
    x = start_x + (27*j)
    y = start_y + (50*j)
    for i in range(n):
        enemy = Picture('enemy.png', x, y, 50, 50, scene)
        monsters.append(enemy)
        x += 55
    n -= 1

move_right = False
move_left = False

speed_x = 3
speed_y = 3


while True:
    wn.fill(scene)
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    for enemy in monsters:
        enemy.draw()
        if ball.colliderect(enemy.rect):
            monsters.remove(enemy)
            speed_y *= -1
    ball.draw()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True      
            elif event.key == pygame.K_a:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
    platform.draw()
    if move_right:
        platform.rect.x += 5
    if move_left:
        platform.rect.x -= 5
    if ball.colliderect(platform.rect):
        speed_y *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1
    if ball.rect.y > (platform.rect.y + 20):
        time_text = pygame.font.SysFont('verdana', 20).render('YOU LOSE', True, (255, 0, 0))
        wn.blit(time_text, (200, 200))
        break
    if len(monsters) == 0:
        time_text = pygame.font.SysFont('verdana', 20).render('YOU WIN', True, (255, 0, 0))
        wn.blit(time_text, (200, 200))
        break

        
                    
           


    clock.tick(40)
    pygame.display.update()
pygame.display.update()
