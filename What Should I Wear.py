import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

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

Show_Result = False

Colour_1 = White
Colour_2 = White

x_coordinate = 200
y_coordinate = 125

Y = False
N = False

run = True
while run:

    screen.fill((0, 205, 255))

    draw_text("What Should I Wear?", text_font, White, 125, 50)

    Question_or_Result(Questions, text_font_Q, Colour_1, x_coordinate, y_coordinate)

    Small_Text(Degree, text_font_D, Colour_2, 200, 175)

    Small_Text("Use Y for yes and N for no.", text_font_D, Colour_2, 225, 350)

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
        Colour_1 = Blue
        Colour_2 = ((0, 205, 255))
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
        Colour_1 = ((175, 100, 0))
        if N == True:
            N = False
            clock.tick(1)
            Questions = Snowing
            if Sandals == True or Hot_Temp == True or Normal_Temp == True:
                Show_Result = True
            if Cold_Temp == True:
                Questions = A_Lot_Snow
        if Y == True:
            Y = False
            Sandals = False
            Sneakers = False
            Winter_Boots = False
            Rain_Boots = True
            clock.tick(1)
            Questions = Snowing
            if Sandals == True or Hot_Temp == True or Normal_Temp == True:
                Show_Result = True
            if Cold_Temp == True:
                Questions = A_Lot_Snow

    if Questions == Snowing:
        Colour_1 = White
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
        x_coordinate = 150
        Colour_1 = White
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
        x_coordinate = 100
        Colour_1 = White
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


    if Show_Result == True:
        screen.fill((0, 205, 255))
        draw_text("What Should I Wear?", text_font, White, 125, 50)
        if Sandals == True:
            Colour_1 = Red
            Result_Shoe = ("You should wear sandals ")
        if Sneakers == True:
            Colour_1 = Green
            Result_Shoe = ("You should wear sneakers ")
        if Winter_Boots == True:
            Colour_1 = White
            Result_Shoe = ("You should wear winter boots ")
        if Rain_Boots == True:
            Colour_1 = Blue
            Result_Shoe = ("You should wear rain boots, ")
        if Long_Pants == True:
            Result_Pants = ("long pants, ")
        if Shorts == True:
            Result_Pants = ("shorts, ")
        if Winter_Coat == True:
            Result_Coat = ("winter coat, ")
        if Light_Coat == True:
            Result_Coat = ("light coat, ")
        if Rain_Coat == True:
            Result_Coat = ("raincoat or umbrella, ")
        if No_Coat == True:
            Result_Coat = ("no coat, ")
        if Long_Sleeve_Shirt == True:
            Result_Shirt = ("long sleeve shirt, ")
        if T_Shirt == True:
            Result_Shirt = ("t-shirt, ")
        if Hoodie == True:
            Result_Hoodie = ("hoodie, ")
        if Hoodie == False:
            Result_Hoodie = ("no hoodie, ")
        if Sunglasses == True:
            Result_Accesory = ("sunglasses, and you ready!")
        if Beanie == True:
            Result_Accesory = ("a beanie, and you ready!")
        if Beanie == False and Sunglasses == False:
            Result_Accesory = ("and your ready!")

        Question_or_Result(Result_Shoe, text_font_Q, Colour_1, 100, 100)
        Question_or_Result(Result_Pants, text_font_Q, Colour_1, 100, 150)
        Question_or_Result(Result_Shirt, text_font_Q, Colour_1, 100, 200)
        Question_or_Result(Result_Coat, text_font_Q, Colour_1, 100, 250)
        Question_or_Result(Result_Hoodie, text_font_Q, Colour_1, 100, 300)
        Question_or_Result(Result_Accesory, text_font_Q, Colour_1, 100, 350)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()


pygame.quit()
