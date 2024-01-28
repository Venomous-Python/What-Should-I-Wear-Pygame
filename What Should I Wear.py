import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Dark_Brown = (130, 70, 0)
Brown = (175, 100, 0)
Grey = (200, 200, 200)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


clock = pygame.time.Clock()

text_font = pygame.font.SysFont("Oswald", 50)

text_font_Q = pygame.font.SysFont("Oswald", 40)

text_font_D = pygame.font.SysFont("Oswald", 20)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def Question_or_Result(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def Small_Text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

pygame.display.set_caption('image')



Freezing = ("Is it Freezing?")

Cold = ("Is it Cold?")

Normal = ("Is it Normal?")

Hot = ("Is it Hot?")

Burning_Hot = ("Is it Burning Hot?")

Rain = ("Is it Raining?")

Mud = ("Is it Muddy?")

Snowing = ("Is it Snowing?")

A_Lot_Snow = ("Is there a lot of Snow?")

Little_Snow = ("Is there a little amount of Snow?")

Troll = ("Stop Trolling!")
Troll_1 = ("I'm Serious!")
Troll_2 = ("I dare you, do it again...")
Troll_3 = False

Hot_Temp = False
Normal_Temp = False
Cold_Temp = False
Freezing_Temp = False
Raining = False

Questions = Freezing

Degree = ("0 °C or below, 32 °F or below.")

Result_Accesory = False
Result_Coat = False
Result_Hoodie = False
Result_Shirt = False
Result_Pants = False
Result_Shoe = False

Sandals = False
Sneakers = False
Winter_Boots = False
Rain_Boots = False

Beanie = False
Sunglasses = False

Winter_Coat = False
Light_Coat = False
Rain_Coat = False
No_Coat = False

Hoodie = False

Long_Pants = False
Shorts = False

Long_Sleeve_Shirt = False
T_Shirt = False

Muddy = False

Show_Result = False

Colour_1 = White
Colour_2 = White

x_coordinate = 200
y_coordinate = 125

Y = False
N = False

run = True
while run:

    screen.fill((Colour_1))

    draw_text("What Should I Wear?", text_font, Colour_2, 125, 50)

    Question_or_Result(Questions, text_font_Q, Colour_2, x_coordinate, y_coordinate)

    Small_Text(Degree, text_font_D, Colour_2, 200, 175)

    Small_Text("Use Y for yes and N for no.", text_font_D, Black, 225, 350)

    key = pygame.key.get_pressed()
    if key[pygame.K_y] == True:
        clock.tick(1)
        Y = True
    elif key[pygame.K_n] == True:
        clock.tick(1)
        N = True


    if Questions == Freezing:
        x_coordinate = 200
        y_coordinate = 125
        Colour_2 = Grey
        Colour_1 = White
        if N == True:
            N = False
            clock.tick(1)
            Questions = Cold
        if Y == True:
            Y = False
            Long_Pants = True
            Beanie = True
            Winter_Coat = True
            Hoodie = True
            Long_Sleeve_Shirt = True
            Freezing_Temp = True
            Winter_Boots = True
            clock.tick(1)
            Winter_Boots = True
            Questions = Snowing
    
    if Questions == Cold:
        Colour_2 = White
        Colour_1 = ((0, 205, 255))
        Degree = ("1 °C - 10 °C, 33 °F - 50 °F")
        if N == True:
            N = False
            clock.tick(1)
            Questions = Normal
            Sneakers = True
        if Y == True:
            Y = True
            Long_Pants = True
            Light_Coat = True
            Hoodie = True
            Long_Sleeve_Shirt = True
            Cold_Temp = True
            Sandals = False
            Sneakers = True
            Winter_Boots = False
            Rain_Boots = False
            clock.tick(1)
            Questions = Rain
            Y = False
   
    if Questions == Normal:
        Colour_2 = ((255, 150, 0))
        Colour_1 = ((230, 230, 0))
        Degree = ("11 °C - 20 °C, 51 °F - 68 °F")
        if N == True:
            N = False
            clock.tick(1)
            Questions = Hot
            Sneakers = True
        if Y == True:
            No_Coat = True
            Shorts = True
            Normal_Temp = True
            Y = False
            Long_Sleeve_Shirt = True
            Sandals = False
            Sneakers = True
            Winter_Boots = False
            Rain_Boots = False
            clock.tick(1)
            Questions = Rain

    if Questions == Hot:
        Colour_2 = Red
        Colour_1 = ((255, 125, 0))
        Degree = ("21 °C - 30 °C, 69 °F - 86 °F")
        if N == True:
            N = False
            clock.tick(1)
            Questions = Burning_Hot
            Sneakers = True
        if Y == True:
            No_Coat = True
            Shorts = True
            Hot_Temp = True
            Y = False
            T_Shirt = True
            Sandals = False
            Sneakers = True
            Winter_Boots = False
            Rain_Boots = False
            clock.tick(1)
            Questions = Rain
    
    if Questions == Burning_Hot:
        Colour_2 = ((150, 0, 0))
        Colour_1 = Red
        Degree = ("31 °C or above, 87 °F or above")
        if Y == True:
            Y = False
            No_Coat = True
            Shorts = True
            T_Shirt = True
            Sunglasses = True
            Sandals = True
            Sneakers = False
            Winter_Boots = False
            Rain_Boots = False
            clock.tick(1)
            Questions = Mud
        if Y == True:
            Y = False
            clock.tick(1)
            Questions = Burning_Hot
        if N == True:
            N = False
            clock.tick(1)
            Questions = Troll

    
    if Questions == Troll:
        if N == True:
            N = False
            clock.tick(1)
            Questions = Troll_1
        if Y == True:
            Y = False
            clock.tick(1)
            Questions = Freezing
                
    if Questions == Troll_1:
        if N == True:
            N = False
            clock.tick(1)
            Questions = Troll_2
        if Y == True:
            Y = False
            clock.tick(1)
            Questions = Freezing

    if Questions == Troll_2:
        x_coordinate = 100
        if N == True:
            N = False
            Troll_3 = True
        if Y == True:
            Y = False
            clock.tick(1)
            Questions = Freezing

    if Troll_3 == True:
        run = False
        

    if Questions == Rain and Sandals == False:
        Colour_1 = ((0, 225, 255))
        Colour_2 = ((0, 130, 215))
        Degree = (" ")
        if N == True:
            N = False
            clock.tick(1)
            Questions = Mud
        if Y == True:
            Y = False
            Rain_Coat = True
            Rain_Boots = True
            Raining = True
            clock.tick(1)
            Sandals = False
            Sneakers = False
            Winter_Boots = False
            Rain_Boots = True
            Questions = Mud

    if Questions == Mud:
        Colour_2 = Dark_Brown
        Colour_1 = Brown
        if N == True:
            N = False
            clock.tick(1)
            Questions = Snowing
            if Sandals == True or Hot_Temp == True:
                Show_Result = True
            if Cold_Temp == True:
                Questions = A_Lot_Snow
            if Normal_Temp == True and Raining == False:
                Questions = Little_Snow
        if Y == True:
            Y = False
            Sandals = False
            Sneakers = False
            Winter_Boots = False
            Rain_Boots = True
            Muddy = True
            clock.tick(1)
            Questions = Snowing
            if Sandals == True or Hot_Temp == True or Normal_Temp == True:
                Show_Result = True
            if Cold_Temp == True:
                Questions = A_Lot_Snow

    if Questions == Snowing:
        Colour_1 = White
        Colour_2 = Grey
        if N == True:
            N = False
            clock.tick(1)
            Questions = A_Lot_Snow
        if Y == True:
            Y = False
            Sandals = False
            Sneakers = False
            Winter_Boots = True
            Rain_Boots = False
            clock.tick(1)
            Show_Result = True
            
    if Questions == A_Lot_Snow:
        Colour_2 = Grey
        Colour_1 = White
        x_coordinate = 150
        if N == True:
            N = False
            clock.tick(1)
            Questions = Little_Snow
        if Y == True:
            Y = False
            clock.tick(1)
            Show_Result = True
            Sandals = False
            Sneakers = False
            Winter_Boots = True
            Rain_Boots = False
            Show_Result = True
      
    if Questions == Little_Snow:
        Colour_1 = White
        Colour_2 = Grey
        x_coordinate = 100
        if N == True:
            N = False
            clock.tick(1)
            Show_Result = True
        if Y == True:
            Y = False
            if Cold_Temp == True:
                Sandals = False
                Sneakers = True
                Winter_Boots = False
                Rain_Boots = False
                Show_Result = True
            if Cold_Temp == False:
                Sandals = False
                Sneakers = False
                Winter_Boots = True
                Rain_Boots = False
                Show_Result = True
            if Normal_Temp == True and Muddy == False:
                Sandals = False
                Sneakers = True
                Winter_Boots = False
                Rain_Boots = False
                Show_Result = True


    if Show_Result == True:
        screen.fill((0, 205, 255))
        draw_text("What Should I Wear?", text_font, Colour_2, 125, 50)
        if Sandals == True:
            Colour_1 = Red
            Colour_2 = ((150, 0, 0))
            Result_Shoe = ("Sandals")
            image = pygame.image.load('Sandals.png')
            screen.blit(image,(375, 275))
        if Sneakers == True:
            Colour_1 = ((230, 230, 0))
            Colour_2 = ((255, 150, 0))
            Result_Shoe = ("Sneakers")
            image = pygame.image.load('Sneakers.png')
            screen.blit(image,(375, 275))
        if Winter_Boots == True:
            Colour_1 = White
            Colour_2 = Grey
            Result_Shoe = ("Winter Boots")
            image = pygame.image.load('Winter Boots.png')
            screen.blit(image,(375, 275))
        if Rain_Boots == True:
            Colour_1 = ((0, 225, 255))
            Colour_2 = ((0, 130, 215))
            Result_Shoe = ("Rain Boots")
            image = pygame.image.load('Rain Boots.png')
            screen.blit(image,(375, 275))
        if Long_Pants == True:
            Result_Pants = ("Long Pants")
            image = pygame.image.load('Long Pants.png')
            screen.blit(image,(375, 75))
        if Shorts == True:
            Result_Pants = ("Shorts")
            image = pygame.image.load('Shorts.png')
            screen.blit(image,(375, 75))
        if Winter_Coat == True:
            Result_Coat = ("Winter coat")
            image = pygame.image.load('Winter Coat.png')
            screen.blit(image,(75, 275))
        if Light_Coat == True:
            Result_Coat = ("Light coat")
            image = pygame.image.load('Light Coat.png')
            screen.blit(image,(75, 275))
        if Rain_Coat == True:
            Result_Coat = ("Raincoat")
            image = pygame.image.load('Raincoat.png')
            screen.blit(image,(75, 275))
        if No_Coat == True:
            Result_Coat = ("No coat, ")
        if Long_Sleeve_Shirt == True:
            Result_Shirt = ("long sleeve shirt, ")
            image = pygame.image.load('Long Sleeve Shirt.png')
            screen.blit(image,(225, 275))
        if T_Shirt == True:
            Result_Shirt = ("T-shirt")
            image = pygame.image.load('T Shirt.png')
            screen.blit(image,(225, 275))
        if Hoodie == True:
            Result_Hoodie = ("Hoodie")
            image = pygame.image.load('Hoodie.png')
            screen.blit(image,(225, 75))
        if Hoodie == False:
            Result_Hoodie = ("No hoodie")
        if Sunglasses == True:
            Result_Accesory = ("Sunglasses")
            image = pygame.image.load('Sunglasses.png')
            screen.blit(image,(75, 75))
        if Beanie == True:
            Result_Accesory = ("Beanie")
            image = pygame.image.load('Beanie.png')
            screen.blit(image,(75, 75))
        if Rain_Coat == True:
            image = pygame.image.load('Umbrella.png')
            screen.blit(image,(75, 75))
            Result_Accesory = ("Umbrella")
        if Rain_Coat == False and Beanie == False and Sunglasses == False:
            Result_Accesory = ("No accessory")

        Small_Text(Result_Shoe, text_font_D, Black, 375, 375)
        Small_Text(Result_Pants, text_font_D, Black, 375, 175)
        Small_Text(Result_Shirt, text_font_D, Black, 225, 375)
        Small_Text(Result_Coat, text_font_D, Black, 75, 375)
        Small_Text(Result_Hoodie, text_font_D, Black, 225, 175)
        Small_Text(Result_Accesory, text_font_D, Black, 75, 175)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()


pygame.quit()
