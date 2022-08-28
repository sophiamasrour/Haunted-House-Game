# Sophia Masrour    sim7fv

import gamebox
import pygame
camera = gamebox.Camera(800, 600)


player_sheet = gamebox.load_sprite_sheet('https://www.codeandweb.com/blog/2016/05/10/how-to-create-a-sprite-sheet/spritestrip.png', 1, 6)
num_frames = 6
curr_image = 0

player = gamebox.from_color(30, 575, "red", 40, 40)
player.image = player_sheet[curr_image]

skeleton_sheet = gamebox.load_sprite_sheet('https://i.stack.imgur.com/C3ZwL.png', 4, 9)
curr_image_skel = 27
curr_image_skel_2 = 27

door_sheet = gamebox.load_sprite_sheet('https://i.pinimg.com/originals/a7/ae/ed/a7aeed46277d4d5680a41193baf17bcb.png', 4, 3)

curr_image_door = 2

knife_url = 'https://freepngimg.com/thumb/knife/27721-3-knife-clipart-thumb.png'

background = gamebox.from_color(400, 300, "grey", 800, 600)
background.image = 'https://png.pngtree.com/thumb_back/fw800/background/20191009/pngtree-horror-grunge-wall-texture-background-image_318769.jpg'


############################################### INTRO ############################################################
name = gamebox.from_text(camera.x, camera.y - 150, "Escape from Mystic Manor", 70, 'red')
str1 = "Oh no, you've woken up in Mystic Manor! Press the arrow keys to move back and forth, and the space bar to jump."
str2 = "You only have one life per level so make sure you don't touch any of the monsters or booby traps."
str3 = "Escape before time runs out to make it to the next level. Good luck!"
str4 = 'SELECT LEVEL: Press 1 for EASY, Press 2 for MEDIUM, and Press 3 for HARD'
description1 = gamebox.from_text(camera.x, camera.y + 80,  str1, 20, 'red')
description2 = gamebox.from_text(camera.x, camera.y + 95,  str2, 20, 'red')
description3 = gamebox.from_text(camera.x, camera.y + 110,  str3, 20, 'red')
description4 = gamebox.from_text(camera.x, camera.y + 150,  str4, 25, 'red')
description5 = gamebox.from_text(camera.x, camera.y + 190,  'PRESS THE SPACE BAR TO START', 25, 'red')
intro = [background, name, description1, description2, description3, description4, description5]

message1 = gamebox.from_text(camera.x, camera.y, 'GAME OVER', 60, 'red')
message2 = gamebox.from_text(camera.x, camera.y + 100, "Press the space bar to try again", 35, 'red')

###################################################### LEVEL 1 ####################################################


ground_1 = gamebox.from_color(400, 600, "black", 800, 30)
leftwall_1 = gamebox.from_color(0, 300, "black", 30, 600)
rightwall_1 = gamebox.from_color(800, 300, "black", 30, 600)
topwall_1 = gamebox.from_color(400, 0, "black", 800, 30)

obstacles_1 = [ground_1, leftwall_1, rightwall_1, topwall_1]

enemy_1 = gamebox.from_color(100, 415, 'purple', 30, 40)
enemy_1.image = skeleton_sheet[27]
enemy_1.xspeed = 5

knives_list1_1 = []
knives_list2_1 =[]

platform1_1 = gamebox.from_color(300, 450, "black", 600, 50)
platform2_1 = gamebox.from_color(550, 290, "black", 500, 50)
platform3_1 = gamebox.from_color(200, 130, "black", 500, 50)

platforms_1 = [platform1_1, platform2_1, platform3_1]

token1_1= gamebox.from_color(75, 315, 'yellow', 25, 25)
token1_1.image = 'https://freepngimg.com/thumb/key/15-golden-key-png-image--thumb.png'
token_list_1 = [token1_1]


exit_1 = gamebox.from_image(25, 80, door_sheet[1])


timer = 130


##################################### MEDIUM #################################################

enemy_2 = gamebox.from_color(400, 280, 'purple', 30, 40)
enemy_2.image = skeleton_sheet[27]
enemy_2.xspeed = 5

token1_2 = token1_1 = gamebox.from_color(725, 200, 'yellow', 25, 25)
token1_2.image = 'https://freepngimg.com/thumb/key/15-golden-key-png-image--thumb.png'
token_list_2 = [token1_1, token1_2]


#################################### WINNER ###################################################

strw1 = "Congratulations!"
strw2 = 'You\'ve escaped Mystic Manor'
strw3 = "To play another level, please restart the game."
win_message_1 = gamebox.from_text(camera.x, camera.y -100, strw1, 60, 'red')
win_message_2 = gamebox.from_text(camera.x, camera.y, strw2, 30, 'red')
win_message_3 = gamebox.from_text(camera.x, camera.y +100, strw3, 30, 'red')

winner_list = [win_message_1, win_message_2, win_message_3]


##################################################################################################

start_game_1 = False
game_over_1 = False
intro_screen = True

winner = False

tps = 0

stepcount_1 = 0


def tick (keys):
    global intro_screen
    global start_game_1
    global winner
    global tps
    global timer
    global game_over_1
    global stepcount_1
    global curr_image
    global enemy_1
    global curr_image_skel
    global tps_l1
    global curr_image_door
    ##### START SCREEN ####
    if intro_screen == True:
        for each in intro:
            camera.draw(each)
        camera.display()

    ##### LEVEL INTRO #####
    if start_game_1 == False:
        if pygame.K_SPACE in keys:
            intro_screen = False
            start_game_1 = True


    ############################################ LEVEL 1 GAME ########################################################
    if start_game_1 == True:
        camera.draw(background) #MAYBE
        ######### MOVEMENT ############
        if player.touches(ground_1):
            if pygame.K_SPACE in keys:
                player.yspeed -= 10
                player.move_speed()
        if player.touches(platform1_1):
            if pygame.K_SPACE in keys:
                player.yspeed -= 10
                player.move_speed()
        if player.touches(platform2_1):
            if pygame.K_SPACE in keys:
                player.yspeed -= 10
                player.move_speed()
        if pygame.K_RIGHT in keys:
            player.x += 6
            stepcount_1 += 0.5
            curr_image = int(stepcount_1) % num_frames
            player.image = player_sheet[curr_image]
        if pygame.K_LEFT in keys:
            player.x -= 6
            stepcount_1 += 0.5
            curr_image = int(stepcount_1) % num_frames
            player.image = player_sheet[curr_image]
        player.yspeed += 0.25
        player.move_speed()


       ##### ENEMY MOVEMENT ######
        if enemy_1.x >= 590:
            enemy_1.xspeed *= -1
            enemy_1.flip()
            enemy_1.move_speed()
        if enemy_1.x <= 35:
            enemy_1.xspeed *= -1
            enemy_1.flip()
            enemy_1.move_speed()
        if enemy_1.touches(platform1_1):
            enemy_1.move_to_stop_overlapping(platform1_1)

        enemy_1.move_speed()

        tps += 1
        if tps % 2 == 0:
            curr_image_skel +=1
            if curr_image_skel == 36:
                curr_image_skel = 28
            else:
                enemy_1.image = skeleton_sheet[curr_image_skel]

##### KNIVES ######
        if tps % 150 == 0:
            new_knife1_1 = gamebox.from_color(820, 558, 'yellow', 45, 30)
            new_knife1_1.image = knife_url
            new_knife1_1.xspeed = -10
            knives_list1_1.append(new_knife1_1)
            new_knife2_1 = gamebox.from_color(-20, 253, 'yellow', 45, 30)
            new_knife2_1.image = knife_url
            new_knife2_1.flip()
            new_knife2_1.xspeed = 10
            knives_list2_1.append(new_knife2_1)

        if tps > 150:
            for each in knives_list1_1:
                if each.x <= -20:
                    knives_list1_1.remove(each)
                else:
                    each.move_speed()
                if each.touches(player):
                    game_over_1 = True
            for each in knives_list2_1:
                if each.x >= 820:
                    knives_list2_1.remove(each)
                else:
                    each.move_speed()
                if each.touches(player):
                    game_over_1 = True


        #### TIMER ##########

        if tps % 30 == 0:
            timer -= 1
        timer_box = gamebox.from_text(camera.x + 250, 30, "Time Remaining: " + str(timer).zfill(3), 25, "red")
        camera.draw(timer_box)
        if player.touches(enemy_1):
            game_over_1 = True
        if timer <= 0:
            game_over_1 = True



    ########## OBSTACLE TOUCHING ###########
        for each in obstacles_1:
            if player.touches(each):
                player.move_to_stop_overlapping(each)
        for each in platforms_1:
            if player.touches(each):
                player.move_to_stop_overlapping(each)
        if exit_1.touches(leftwall_1):
            exit_1.move_to_stop_overlapping(leftwall_1)
        if exit_1.touches(platform3_1):
            exit_1.move_to_stop_overlapping(platform3_1)

        for each in knives_list1_1:
            if player.touches(each):
                game_over_1 = True
        for each in knives_list2_1:
            if player.touches(each):
                game_over_1 = True

    ### TOKEN TOUCHING ####

        if len(token_list_1) > 0:
            if player.touches(token1_1):
                del token_list_1[0]
                tps_l1 = tps
        if len(token_list_1) == 0:
            if curr_image_door == 11:
                exit_1.image = door_sheet[curr_image_door]
            else:
                if tps == tps_l1 + 15:
                    exit_1.image = door_sheet[4]
                    curr_image_door += 3
                elif tps == tps_l1 + 30:
                    exit_1.image = door_sheet[7]
                    curr_image_door += 3
                elif tps == tps_l1 + 45:
                    exit_1.image = door_sheet[10]


    #### LEVEL COMPLETION #######
        if player.touches(exit_1):
            start_game_1 = False
            winner = True


        for each in knives_list1_1:
            camera.draw(each)
        for each in knives_list2_1:
            camera.draw(each)
        for each in obstacles_1:
            camera.draw(each)
        for each in platforms_1:
            camera.draw(each)
        camera.draw(exit_1)
        camera.draw(player)
        camera.draw(enemy_1)
        camera.draw(timer_box)
        if len(token_list_1) > 0:
            for each in token_list_1:
                camera.draw(each)
        camera.display()

        if game_over_1 == True:
            start_game_1 = False
            camera.clear('grey')
            camera.draw(message1)
            camera.draw(message2)
            camera.display()
            timer = 130
            player.center = [30, 575]
            if pygame.K_SPACE in keys:
                start_game_1 = True
                game_over_1 = False
                if len(token_list_1) == 0:
                    token_list_1.append(token1_1)
                    exit_1.image = door_sheet[1]
    if winner == True:
        camera.clear('grey')
        for each in winner_list:
            camera.draw(each)
        camera.display()







ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
