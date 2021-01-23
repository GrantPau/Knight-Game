import pygame
from random import randrange

pygame.init()

size = width, height = 600, 400
black = (0,0,0)
white = (255,255,255)
red = (243, 42, 42)
yellow = (255, 255, 0)
blue = (175, 238, 238)
blue2 = (150, 210, 210)
blue3 = (93, 126, 168)
blue4 = (46, 75, 114)
green = (173, 255, 47)
limegreen = (50, 205, 50)
grey = (152, 152, 152)
lightgrey = (179, 179, 179)
brown = (140,110,100)
darkbrown = (109,77,66)
eggwhite = (249,250,252)
darkwhite = (190,187,195)
#Sun
sunEast = 130
sunWest = 20
sunSouth = 95
sunNorth = -15
speed = 0.25
score = 0
score_counter = 0
check_counter = 0
double_jumps = 0
lives = 3
move_up = None
move_down = None
move_left = None
move_right = None
score_boolean = True
screen_boolean = False
start_game = False
main_menu = True
instructions_menu = False
controls_menu = False
block_speed = -2
was_pressed = False

screen = pygame.display.set_mode(size)

select_sound = pygame.mixer.Sound("SelectSound.wav")
jump_sound = pygame.mixer.Sound("JumpSound.wav")
collision_sound = pygame.mixer.Sound("CollisionSound.wav")
retry_sound = pygame.mixer.Sound("RetrySound.wav")

class Mountain(pygame.sprite.Sprite):
    def __init__(self, x, y, heights):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([400, 400], pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect() #make the x and y
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 2
        self.heights = heights
        pygame.draw.polygon(self.image, brown, [(self.rect.x, self.rect.y), (self.rect.x + 100, self.rect.y), (self.rect.x + 50, self.rect.y - self.heights)])
        pygame.draw.polygon(self.image, darkbrown, [(self.rect.x + 50, self.rect.y), (self.rect.x + 100, self.rect.y),
                                                    (self.rect.x + 50, self.rect.y - self.heights)])
        pygame.draw.polygon(self.image, eggwhite, [(self.rect.x + 50, self.rect.y - self.heights), (self.rect.x + 50, (self.rect.y - self.heights) + (self.heights / 2)),
                                                (self.rect.x + 25, (self.rect.y - self.heights) + (self.heights / 2))])
        pygame.draw.polygon(self.image, darkwhite, [(self.rect.x + 50, self.rect.y - self.heights),
                                                (self.rect.x + 50, (self.rect.y - self.heights) + (self.heights / 2)),
                                                (self.rect.x + 75, (self.rect.y - self.heights) + (self.heights / 2))])

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.x > width:
            self.rect.x = -self.rect.x

class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([400, 400], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = randrange(1, 3)
        self.w = w
        self.h = h
        pygame.draw.circle(self.image, eggwhite,[int(self.w / 2), int(self.h / 8)], 25)
        pygame.draw.circle(self.image, eggwhite, [int(self.w / 2 + 40), int(self.h / 8)], 20)
        pygame.draw.rect(self.image, blue2, [self.w / 4, self.h / 4, 100, -25])

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.x > width:
            self.rect.x = -self.w

class Cloud2(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([400, 400], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = randrange(1, 3)
        self.w = w
        self.h = h
        pygame.draw.circle(self.image, eggwhite,[int(self.w / 2), int(self.h / 8)], 25)
        pygame.draw.circle(self.image, eggwhite, [int(self.w / 2 + 40), int(self.h / 8)], 20)
        pygame.draw.rect(self.image, blue3, [self.w / 4, self.h / 4, 100, -25])

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.x > width:
            self.rect.x = -self.w
class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, heights):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([600, 400], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 2
        self.w = w
        self.h = h
        self.heights = heights
        pygame.draw.rect(self.image, darkbrown, [self.w / 2, self.h / 2, 3, -10])
        pygame.draw.polygon(self.image, (46, 80, 23),
                            [(self.w / 2 - 10, self.h / 2 - 10), (self.w / 2 + 10, self.h / 2 - 10),
                             (self.w / 2 + 2, self.h / 2 - self.heights)])
        pygame.draw.polygon(self.image, (31, 55, 15),
                            [(self.w / 2, self.h / 2 - 10), (self.w / 2 + 10, self.h / 2 - 10),
                             (self.w / 2 + 2, self.h / 2 - self.heights)])

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.x > width:
            self.rect.x = -self.w

class Tree2(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, heights):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([400, 400], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 2
        self.w = w
        self.h = h
        self.heights = heights
        pygame.draw.rect(self.image, darkbrown, [self.w / 2, self.h / 2, 3, -10])
        pygame.draw.polygon(self.image, (46, 80, 23),
                            [(self.w / 2 - 10, self.h / 2 - 10), (self.w / 2 + 10, self.h / 2 - 10),
                             (self.w / 2 + 2, self.h / 2 - self.heights)])
        pygame.draw.polygon(self.image, (31, 55, 15),
                            [(self.w / 2, self.h / 2 - 10), (self.w / 2 + 10, self.h / 2 - 10),
                             (self.w / 2 + 2, self.h / 2 - self.heights)])
        pygame.draw.polygon(self.image, (46, 80, 23),
                            [(self.w / 2 - 10, self.h / 2 - 20), (self.w / 2 + 10, self.h / 2 - 20),
                             (self.w / 2 + 2, self.h / 2 - self.heights - 20)])
        pygame.draw.polygon(self.image, (31, 55, 15),
                            [(self.w / 2, self.h / 2 - 20), (self.w / 2 + 10, self.h / 2 - 20),
                             (self.w / 2 + 2, self.h / 2 - self.heights - 20)])

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.x > width:
            self.rect.x = -self.w

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        global block_speed
        self.image = pygame.Surface([30, 30], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = block_speed
        self.w = w
        self.h = h
        pygame.draw.rect(self.image, (randrange(0, 255), randrange(0, 255), randrange(0, 255)), [0, 0, self.w, self.h])

    def update(self):
        global block_speed
        self.rect.x += block_speed
        if self.rect.x < -50:
            self.rect.x = width
            block_speed += -0.2
        global lives
        if lives <= 0:
            self.rect.x = 600
            block_speed = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    block_speed = -2

class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, w, h):
        image = pygame.Surface([100, 100], pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        self.sprite_sheet.set_colorkey(white)
        return image


class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface([50, 50], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 3
        self.change_y = 0
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        self.colliding = None
        self.jump = False
        self.jump_y = 0
        self.gravity = 0.3
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.direction = "R"


        sprite_sheet = SpriteSheet("knight_sprite.png")
        image = pygame.transform.scale(sprite_sheet.get_image(0, 0, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(100, 0, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(200, 0, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(300, 0, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(400, 0, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(500, 0, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(0, 100, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(100, 100, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(200, 100, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(300, 100, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(400, 100, 100, 100), (w, h))
        self.walking_frames_r.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(500, 100, 100, 100), (w, h))
        self.walking_frames_r.append(image)

        image = pygame.transform.scale(sprite_sheet.get_image(0, 0, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(100, 0, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(200, 0, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(300, 0, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(400, 0, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(500, 0, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(0, 100, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(100, 100, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(200, 100, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(300, 100, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(400, 100, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(500, 100, 100, 100), (w, h))
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]

    def update(self):
        global score
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        pos = self.rect.x

        if self.direction == "R":
            frame = (pos // 15) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 15) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        if self.rect.x > width:
            self.rect.x = -self.w
            score += 10
            global check_counter
            check_counter += 1
            if check_counter == 3:
                global double_jumps
                if double_jumps <= 5:
                    double_jumps += 1
                    check_counter = 0
                    if double_jumps == 6:
                        double_jumps = 5
        global lives
        if lives <= 0:
            self.direction = "R"
            self.rect.x = 0
            self.change_x = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.change_x = 3

    def go_up(self):
        def double_jump():
            print("double jumping")
            self.jump = False
            if not self.jump:
                self.jump_y = -6
                self.jump = True
                pygame.mixer.Sound.play(jump_sound)
            elif self.jump:
                global move_left
                global move_right
                global double_jumps
                move_left = False
                move_right = False
                self.jump_y += self.gravity
                self.rect.y += self.jump_y
                if self.rect.y > 250:
                    self.rect.y = 250
                    self.jump_y = 0
                    self.jump = False
                    global move_up
                    move_up = False
        if not self.jump:
            self.direction = "R"
            self.jump_y = -6
            self.jump = True
            pygame.mixer.Sound.play(jump_sound)
        elif self.jump:
            global move_left
            global move_right
            global double_jumps
            move_left = False
            move_right = False
            self.jump_y += self.gravity
            self.rect.y += self.jump_y
            if self.rect.y > 250:
                self.rect.y = 250
                self.jump_y = 0
                self.jump = False
                global move_up
                move_up = False
            elif double_jumps > 0 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    global was_pressed
                    if not was_pressed:
                        double_jumps -= 1
                        double_jump()
                        was_pressed = True
                    else:
                        was_pressed = False

    def go_down(self):
        self.rect.y += 5
    def go_left(self):
        self.rect.x += -7
        self.direction = "L"
    def go_right(self):
        self.rect.x += 5
        self.direction = "R"

    def checkCollision(self, sprite_list):
        col = pygame.sprite.spritecollide(self, sprite_list, True)
        for enemy_collision in col:
            global score
            global lives
            score += 1
            self.colliding = True
            if self.colliding:
                lives -= 1
                self.colliding = False
                pygame.mixer.Sound.play(collision_sound)
        if col:
            block_list.add(Block(700, 270, 30, 30))


sprite_list = pygame.sprite.Group()
knight_list = pygame.sprite.Group()
cloud_list = pygame.sprite.Group()
mountain_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()

class Counter():
    def __init__(self, score):
        self.score = score
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: " + str(self.score), True, white)
        screen.blit(text, (190, 5))

class DoubleJumpScore():
    def __init__(self, jump_score):
        self.jump_score = jump_score
        font = pygame.font.SysFont(None, 25)
        text = font.render("Double Jumps: " + str(self.jump_score), True, white)
        screen.blit(text, (300, 5))

class Number_of_Lives():
    def __init__(self, lives):
        self.lives = lives
        font = pygame.font.SysFont(None, 25)
        text = font.render("Lives: " + str(self.lives), True, white)
        screen.blit(text, (465, 5))

for i in range(0, 4):
    mountain_list.add(Mountain(randrange(0, 300), 150, randrange(50, 150)))

for j in range(0, 2):
    cloud_list.add(Cloud(randrange(0, width), 160, 100, 200))
    sprite_list.add(Cloud2(randrange(0, width), 90, 100, 200))

for k in range(0, 8):
    sprite_list.add(Tree(randrange(0, width - 100), 300, 20, randrange(100, 200), randrange(40, 55)))
    sprite_list.add(Tree2(randrange(0, width - 100), 300, 20, randrange(100, 200), randrange(40, 55)))

block_list.add(Block(600, 270, 30, 30))
knight_list.add(Knight(0, 250, 50, 50))

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if main_menu:
        pygame.draw.rect(screen, blue, [0, 0, 600, 400])
        small_font = pygame.font.SysFont(None, 25)
        play_text = small_font.render("Press P to PLAY", True, black)
        instructions_text = small_font.render("Press I for INSTRUCTIONS", True, black)
        controls_text = small_font.render("Press C for CONTROLS", True, black)
        screen.blit(play_text, (100, 100))
        screen.blit(instructions_text, (100, 150))
        screen.blit(controls_text, (100, 200))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                start_game = True
                main_menu = False
                pygame.mixer.Sound.play(select_sound)
            if event.key == pygame.K_i:
                instructions_menu = True
                main_menu = False
                pygame.mixer.Sound.play(select_sound)
            if event.key == pygame.K_c:
                controls_menu = True
                main_menu = False
                pygame.mixer.Sound.play(select_sound)
    elif instructions_menu:
        pygame.draw.rect(screen, blue, [0, 0, 600, 400])
        small_font = pygame.font.SysFont(None, 25)
        how_to_play_text = small_font.render("> Dodge the moving block by jumping", True, black)
        how_to_play_text2 = small_font.render("> Gain points automatically by staying alive", True, black)
        how_to_play_text3 = small_font.render("> Gain 10 points each time you move past the right most screen", True, black)
        how_to_play_text4 = small_font.render("> Gain a double jump by passing the right most screen 3 times.", True, black)
        how_to_play_text5 = small_font.render("> MAX. 5 Double Jumps", True, black)
        how_to_play_text6 = small_font.render("> You ALWAYS jump to the right regardless of direction.", True, black)
        go_back_text = small_font.render("Press B to go back to MAIN MENU", True, black)
        screen.blit(how_to_play_text, (5, 50))
        screen.blit(how_to_play_text2, (5, 100))
        screen.blit(how_to_play_text3, (5, 150))
        screen.blit(how_to_play_text4, (5, 200))
        screen.blit(how_to_play_text5, (5, 250))
        screen.blit(how_to_play_text6, (5, 300))
        screen.blit(go_back_text, (5, 350))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                instructions_menu = False
                main_menu = True
                pygame.mixer.Sound.play(select_sound)
    elif controls_menu:
        pygame.draw.rect(screen, blue, [0, 0, 600, 400])
        small_font = pygame.font.SysFont(None, 25)
        controls_text1 = small_font.render("> Press LEFT ARROW to move LEFT", True, black)
        controls_text2 = small_font.render("> Press RIGHT ARROW to move RIGHT", True, black)
        controls_text3 = small_font.render("> Press the UP ARROW to JUMP", True, black)
        controls_text4 = small_font.render("> While Jumping in MID AIR, press DOWN ARROW to DOUBLE JUMP", True, black)
        go_back_text = small_font.render("Press B to go back to MAIN MENU", True, black)
        screen.blit(controls_text1, (5, 50))
        screen.blit(controls_text2, (5, 100))
        screen.blit(controls_text3, (5, 150))
        screen.blit(controls_text4, (5, 200))
        screen.blit(go_back_text, (5, 350))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                controls_menu = False
                main_menu = True
                pygame.mixer.Sound.play(select_sound)
    elif start_game:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
                # elif event.key == pygame.K_DOWN:
                # move_down =True
            elif event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_UP:
            # move_up = False
            # if event.key == pygame.K_DOWN:
            # move_down = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
        if move_up:
            Knight = knight_list.sprites()[0]
            Knight.go_up()
        if move_down:
            Knight = knight_list.sprites()[0]
            Knight.go_down()
        if move_left:
            Knight = knight_list.sprites()[0]
            Knight.go_left()
        if move_right:
            Knight = knight_list.sprites()[0]
            Knight.go_right()

        # Update Background and Sprite
        sprite_list.update()
        mountain_list.update()
        knight_list.update()
        cloud_list.update()
        block_list.update()
        screen.fill(blue)

        #Sky and Grass
        pygame.draw.rect(screen, limegreen, (0, 300, 600, 400))
        pygame.draw.rect(screen, blue2, (0, 150, 600, 75))
        pygame.draw.rect(screen, blue3, (0, 75, 600, 75))
        pygame.draw.rect(screen, blue4, (0, 0, 600, 75))

        #Draw Background and Sprite
        cloud_list.draw(screen)
        mountain_list.draw(screen)
        sprite_list.draw(screen)
        block_list.draw(screen)
        knight_list.draw(screen)

        knight_list.sprites()[0].checkCollision(block_list)

        #Sun
        if sunEast == 130 or sunEast == 110:
            speed = speed * -1
        sunEast += speed
        sunWest += speed * -1
        sunSouth += speed
        sunNorth += speed * -1

        pygame.draw.circle(screen, (255, 255, 51), (75, 40), 25)
        pygame.draw.line(screen, (255, 255, 51), (105, 40), (sunEast, 40))
        pygame.draw.line(screen, (255, 255, 51), (45, 40), (sunWest, 40))
        pygame.draw.line(screen, (255, 255, 51), (75, 70), (75, sunSouth))
        pygame.draw.line(screen, (255, 255, 51), (75, 10), (75, sunNorth))

        #score
        if score_boolean:
            score_counter += 1
        if score_counter == 10:
            score += 1
            score_counter = 0

        #lives
        if lives <= 0:
            score_boolean = False
            screen_boolean = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.mixer.Sound.play(retry_sound)
                    score_boolean = True
                    screen_boolean = False
                    lives = 3
                    score = 0
                    check_counter = 0
                    double_jumps = 0

        Counter(score)
        DoubleJumpScore(double_jumps)
        Number_of_Lives(lives)

        #Game Over Screen
        if screen_boolean:
            move_up = False
            pygame.draw.rect(screen, black, [0, 0, 600, 400])
            font = pygame.font.SysFont(None, 100)
            small_font = pygame.font.SysFont(None, 25)
            game_over = font.render("GAME OVER", True, white)
            retry = small_font.render("Press R to Retry", True, white)
            quit_game = small_font.render("Press ESC to Quit", True, white)
            total_score = font.render("Score: " + str(score), True, white)
            screen.blit(game_over, (100, 175))
            screen.blit(retry, (450, 370))
            screen.blit(quit_game, (15, 370))
            screen.blit(total_score, (100, 100))

    pygame.display.update()
    clock.tick(60)
pygame.quit()