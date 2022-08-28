# Sophia Masrour    sim7mfv

import gamebox
import random
camera = gamebox.Camera(800, 250)

dino_sheet = gamebox.load_sprite_sheet(
  "https://upload.wikimedia.org/wikipedia/commons/2/22/Chromium_T-Rex-offline-trex.png",
  1, 6)
cactus_image = 'https://www.tynker.com/projects/images/396cce56f8f0cbe494d66cb68feb6ca80531e193/cacti---cacti1.png'

background = gamebox.from_color(400, 125, "white", 800, 250)
dino = gamebox.from_image (60, 125, dino_sheet[0])
dino.bottom = 195
ground = gamebox.from_color(400, 200, 'black', 800, 10)
intro = gamebox.from_text(camera.x, camera.y, 'PRESS THE SPACE BAR TO BEGIN', 25, 'black')
cacti = []

camera.draw(background)
camera.draw(ground)
camera.draw(dino)
camera.draw(intro)
camera.display()

score = 0
counter = 0
stepper = 1
start_game = False


def tick (keys):
    global score
    global counter
    global stepper
    global start_game
    if start_game == False:    # this is the default screen when the game is not being played
        if pygame.K_SPACE in keys:
            camera.clear('white')
            dino.image = dino_sheet[1]
            dino.y = 150
            cacti.clear()
            score = 0
            camera.draw(dino)
            camera.draw(ground)
            camera.display()
            if pygame.K_SPACE in keys:
                start_game = True
    if start_game == True:
        camera.clear('white')
        if dino.touches (ground) :# if the dino is on the ground then it can jump, this is so it cannot jump in the air
            if pygame.K_SPACE in keys:
                dino.y -= 150
        dino.yspeed += 0.5  # change of y speed make it accelerate, this acts like gravity
        dino.move_speed()
        dino.x += 8   # move dino with camera

        stepper += 1   # this will make the dino's legs move with the stepper so every time tick is the feet move
        if stepper % 2 == 0 :
            dino.image = dino_sheet[2]
        else:
            dino.image = dino_sheet[3]

        if dino.touches (ground):  # to make sure dino and ground to not overlap
            dino.move_to_stop_overlapping(ground)

        camera.x += 8        # moves camera to the right gradually
        ground.x += 8
        counter += 1

        if counter % 50 == 0 :    # this creates new cacti that are randomly spaced
            if counter % 150 != 0:
                new_cactus = gamebox.from_color(camera.x + random.randint(405, 600), 170, "black", 25, random.randint(25, 60))
                new_cactus.bottom = 195
                new_cactus.image = cactus_image
                cacti.append(new_cactus)

        ############ SCORE ##############
        score += 1
        score_box = gamebox.from_text(camera.x + 250, 30, "Score: " + str(score).zfill(5), 25, "black")
        camera.draw(score_box)

        for each in cacti:
            if dino.touches(each):
                camera.draw(gamebox.from_text(camera.x, camera.y, "GAME OVER", 70, "black"))
                camera.draw(score_box)
                dino.image = dino_sheet[5]
                camera.draw(dino)
                camera.display()
                start_game = False
            if each.x < camera.x - 450: # since the random cacti are part of a list, to make sure it does not get too
                cacti.remove(each)      #long I delete them from the list if they move past the left side of the screen
            camera.draw(each)

        camera.draw(ground)
        camera.draw(dino)
        camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)




