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
        if keys[K_s] and self.rect.y < 395:  
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:  
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)
        self.speed_x = player_speed
        self.speed_y = player_speed
    
    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        

        if self.rect.y <= 0 or self.rect.y >= 500 - self.rect.height:
            self.speed_y *= -1
        
   
        if self.rect.x <= 0:
            return "right"  
        if self.rect.x >= 700 - self.rect.width:
            return "left"  
        
   
        if sprite.collide_rect(self, player1) or sprite.collide_rect(self, player2):
            self.speed_x *= -1
        
        return None

init()
FPS = 60
clock = time.Clock()


score1 = 0
score2 = 0

font.init()
font1 = font.Font(None, 36)

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')


player1 = Player('ping_pong/racket.png', 10, 200, 4, 80, 100)
player2 = Player('ping_pong/racket.png', 600, 200, 4, 80, 100)
ball = Ball('ping_pong/ball.png', 350, 250, 3, 30, 30) 

score_text1 = font1.render('Счет: ' + str(score1), True, (255, 255, 255))
score_text2 = font1.render('Счет: ' + str(score2), True, (255, 255, 255))

winTXT1 = font1.render('Победа первого игрока!', True, (255, 255, 255))
winTXT2 = font1.render('Победа второго игрока!', True, (255, 255, 255))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
     
        result = ball.update()
        if result == "right":
            score2 += 1
            score_text2 = font1.render('Счет: ' + str(score2), True, (255, 255, 255))
         
            ball.rect.x = 350
            ball.rect.y = 250
            ball.speed_x = 3
        elif result == "left":
            score1 += 1
            score_text1 = font1.render('Счет: ' + str(score1), True, (255, 255, 255))
    
            ball.rect.x = 350
            ball.rect.y = 250
            ball.speed_x = -3
        
    
        if score1 >= 5:
            finish = True
            window.blit(winTXT1, (200, 200))
        elif score2 >= 5:
            finish = True
            window.blit(winTXT2, (200, 200))
        
    
        window.fill((95, 158, 160))
        
   
        window.blit(score_text1, (10, 10))
        window.blit(score_text2, (500, 10))
        
      
        player1.reset()
        player2.reset()
        ball.reset()
        
        player1.update_l()
        player2.update_r()
        
    
    
    clock.tick(FPS)
    display.update()
