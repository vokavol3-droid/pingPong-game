from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed

init()
FPS = 60
clock = time.Clock()

font.init()
font1 = font.Font(None, 36)

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')

player1 = Player('ping_pong/racket.png', 10, 250, 4, 80, 100)
player2 = Player('ping_pong/racket.png', 600, 250, 4, 80, 100)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((95, 158, 160))

    player1.reset()
    player2.reset()

    player1.update_l()
    player2.update_r()
    
    clock.tick(FPS)
    display.update()