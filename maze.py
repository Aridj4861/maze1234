from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_a] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_d] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
   direction = "left"
   def update(self):
       if self.rect.x <= 470:
           self.direction = "right"
       if self.rect.x >= win_width - 85:
           self.direction = "left"
 
       if self.direction == "left":
           self.rect.x -= self.speed
       else:
           self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3,wall_width,wall_height,wall_x,wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3 #color_2 и color_3 аналогично   
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall(96,96,96,25,400,75,0)
w2 = Wall(96,96,96,10000,25,75,75)
w3 = Wall(96,96,96,25,350,185,185)
w4 = Wall(96,96,96,25,200,320,185)
w5 = Wall(96,96,96,300,25,320,185)
w6 = Wall(96,96,96,225,25,320,385)
w7 = Wall(96,96,96,25,225,545,385)




 
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
#Персонажи игры:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
 
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
 
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
    
 
        player.reset()
        monster.reset()
        final.reset()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
 
       #Ситуация "Выигрыш"
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()
 
    display.update()
    clock.tick(FPS)
 






