import colorama
import numpy
import bricks
import slider
import sys
import os
import time
import ball
import collision
import global_vars as gb
import bullets


class display:
    def __init__(self):
        # gb.display = [[-1]*122]*36
        gb.display = numpy.array(gb.display)
        self.length = 0

    def createlvl(self, bricks):
        for brick in bricks:
            x = 0
            while x < 4:
                gb.display[brick.Ycor][brick.Xcor+x] = brick.lvl
                x += 1

    def bringbricksdown(self):
        for y in range(35, 0, -1):
            x = 0
            while x < 122:
                if gb.display[y][x] == 0 or gb.display[y][x] == 1 or gb.display[y][x] == 2 or gb.display[y][x] == 3 or gb.display[y][x] == 4 or gb.display[y][x] == 69 or gb.display[y][x] == 111:
                    gb.display[y+1][x] = gb.display[y][x]
                    gb.display[y][x] = -1
                x += 1

    def clearAllPowerUps(self):
        for y in range(35, 0, -1):
            x = 0
            gb.powerup = []
            while x < 122:
                if gb.display[y][x] != 12301 or gb.display[y][x] != 12302 or gb.display[y][x] != 12303 or gb.display[y][x] != 12304 or gb.display[y][x] != 12305 or gb.display[y][x] != 12306:
                    gb.display[y][x] = -1
                x += 1
    def clearAllBullets(self):
        
        gb.bullets = []
           

    def createPowerUP(self, powerUp, set):

        if powerUp.Ycor < 32:
            gb.display[powerUp.Ycor+3][powerUp.Xcor] = powerUp.powerupNum
            gb.display[powerUp.Ycor+1][powerUp.Xcor] = -1
            print(gb.display[powerUp.Ycor][powerUp.Xcor], "pu below")
            if powerUp.Ycor+5 < 36:
                if gb.display[powerUp.Ycor+3][powerUp.Xcor] == 2019111026 or gb.display[powerUp.Ycor+4][powerUp.Xcor] == 2019111026 or gb.display[powerUp.Ycor+5][powerUp.Xcor] == 2019111026:
                    collision1 = collision.collision()
                    collision1.puwithpadle(powerUp, set)
            else:
                if gb.display[powerUp.Ycor+3][powerUp.Xcor] == 2019111026 or gb.display[powerUp.Ycor+4][powerUp.Xcor] == 2019111026:
                    collision1 = collision.collision()
                    collision1.puwithpadle(powerUp, set)
        elif powerUp.Ycor < 34:
            gb.display[powerUp.Ycor][powerUp.Xcor] = -1
            gb.display[powerUp.Ycor+1][powerUp.Xcor] = -1

    def updateSlider(self, slider):
        # print(slider,"display")
        self.length = slider.slider_length
        # print(self.length, slider.slider_length, "len")
        if slider.Xcor > 0 and slider.Xcor < 114:
            x = 0
            while x < slider.slider_length:
                gb.display[slider.Ycor][slider.Xcor+x] = 2019111026
                x += 1
            for a in range(0, slider.Xcor):
                gb.display[slider.Ycor][a] = -1
            for b in range(slider.Xcor+slider.slider_length, 122):
                gb.display[slider.Ycor][b] = -1
        # print(slider.Xcor,"gorhoepwgnp")
        # print(slider.slider_length,"gorhoepwgnp")

    def dropPowerUP(self, powerups, set):
        for powerup in powerups:
            powerup = powerup.dpp()
            self.createPowerUP(powerup, set)
        return powerups

    def lvlup(self):
        self.clearAllPowerUps()
        self.clearAllBullets()
        print("lvl" + str(gb.Current_lvl+1) + "Approaching")
        # gb.display[35] = -1
        # time.sleep(2)
        gb.Xspeed = 0
        gb.Yspeed = -1
        gb.motionUp = True
        gb.motionRight = True
        gb.grab = True
        gb.exp = False
        gb.thru = False
        gb.pugrab = False
        gb.Current_lvl += 1

    def sliderShoot(self,set):
        gb.bullets.append(bullets.bullet(set.slider.Ycor - 1, set.slider.Xcor))        
        gb.bullets.append(bullets.bullet(set.slider.Ycor - 1, set.slider.Xcor+ self.length -1))        
        for bullet in gb.bullets:
            gb.display[bullet.Ycor][bullet.Xcor] = 8
    
    def moveBulletUp(self):
        for bullet in gb.bullets:
            if bullet.Ycor > 1:
                bullet.moveup()
                gb.display[bullet.Ycor][bullet.Xcor] = 8
                gb.display[bullet.Ycor+1][bullet.Xcor] = -1
            else:
                gb.display[bullet.Ycor][bullet.Xcor] = -1
            if gb.display[bullet.Ycor-1][bullet.Xcor] != -1 and (gb.display[bullet.Ycor-1][bullet.Xcor] != 12301 or gb.display[bullet.Ycor-1][bullet.Xcor] != 12302 or gb.display[bullet.Ycor-1][bullet.Xcor] != 12303 or gb.display[bullet.Ycor-1][bullet.Xcor] != 12304 or gb.display[bullet.Ycor-1][bullet.Xcor] != 12305 or  gb.display[bullet.Ycor-1][bullet.Xcor] != 12306) and gb.display[bullet.Ycor-1][bullet.Xcor] != 8:
                if  gb.display[bullet.Ycor-1][bullet.Xcor] != 4:
                    collision1 = collision.collision()
                    collision1.bulletWithTop(bullet.Ycor-1, bullet.Xcor)
                gb.display[bullet.Ycor][bullet.Xcor] = -1
                bullet.disappear()



    def updateBall(self, set, ball, Yspeed, Xspeed):
        col = True
        if ball.Xcor-1 <= 0:
            collision1 = collision.collision()
            collision1.withLeft(ball.Ycor, ball.Xcor)
        elif ball.Xcor+Xspeed >= 121:
            collision1 = collision.collision()
            collision1.withRight(ball.Ycor, ball.Xcor)
        elif ball.Ycor-1 == 0:
            collision1 = collision.collision()
            collision1.withTop(ball.Ycor, ball.Xcor)
        elif ball.Ycor+1 > 35:
            gb.display[34] = -1
            gb.lives -= 1
            ball.updateYX(set.slider.Ycor-1, set.slider.Xcor+3)
            gb.Xspeed = 0
            gb.Yspeed = -1
            gb.motionUp = True
            gb.grab = True
            gb.thru = False
            gb.motionRight = True
            if gb.lives < 0:
                print("Game Over")
                sys.exit(0)
        else:
            if gb.motionUp and col:
                if gb.display[ball.Ycor-1][ball.Xcor] != -1 and (gb.display[ball.Ycor-1][ball.Xcor] != 12301 or gb.display[ball.Ycor-1][ball.Xcor] != 12302 or gb.display[ball.Ycor-1][ball.Xcor] != 12303 or gb.display[ball.Ycor-1][ball.Xcor] != 12304 or gb.display[ball.Ycor-1][ball.Xcor] != 12305 or  gb.display[ball.Ycor-1][ball.Xcor] != 12306 or gb.display[ball.Ycor-1][ball.Xcor] != 12307) and gb.display[ball.Ycor-1][ball.Xcor] != 8:
                    collision1 = collision.collision()
                    col = False
                    collision1.withTop(ball.Ycor-1, ball.Xcor)

            elif not(gb.motionUp) and col:
                print(ball.Xcor, ball.Ycor, "debug")
                if gb.display[ball.Ycor+1][ball.Xcor] != -1 and (gb.display[ball.Ycor+1][ball.Xcor] != 12301 or gb.display[ball.Ycor+1][ball.Xcor] != 12302 or gb.display[ball.Ycor+1][ball.Xcor] != 12303 or gb.display[ball.Ycor+1][ball.Xcor] != 12304 or gb.display[ball.Ycor+1][ball.Xcor] != 12305 or gb.display[ball.Ycor+1][ball.Xcor] != 12306 or gb.display[ball.Ycor+1][ball.Xcor] != 12307) and gb.display[ball.Ycor+1][ball.Xcor] != 8:
                    collision1 = collision.collision()
                    col = False
                    collision1.withBottom(ball.Ycor+1, ball.Xcor)
                    if gb.display[ball.Ycor+1][ball.Xcor] == 2019111026:
                        

                        # print("suyahsd dha;idgh;i")
                        self.bringbricksdown()

            if gb.motionRight and col:
                if gb.display[ball.Ycor][ball.Xcor+1] != -1 and gb.display[ball.Ycor][ball.Xcor+1] != 2019111026 and (gb.display[ball.Ycor][ball.Xcor+1] != 12301 or gb.display[ball.Ycor][ball.Xcor+1] != 12302 or gb.display[ball.Ycor][ball.Xcor+1] != 12303 or gb.display[ball.Ycor][ball.Xcor+1] != 12304 or gb.display[ball.Ycor][ball.Xcor+1] != 12305 or gb.display[ball.Ycor][ball.Xcor+1] != 12306 or gb.display[ball.Ycor][ball.Xcor+1] != 12307) and gb.display[ball.Ycor][ball.Xcor+1] != 8:
                    collision1 = collision.collision()
                    col = False
                    collision1.withRight(ball.Ycor, ball.Xcor+1)

            elif not(gb.motionRight) and col:
                if gb.display[ball.Ycor][ball.Xcor-1] != -1 and gb.display[ball.Ycor][ball.Xcor-1] != 2019111026 and gb.display[ball.Ycor][ball.Xcor-1] != 8:
                    collision1 = collision.collision()
                    col = False
                    collision1.withLeft(ball.Ycor, ball.Xcor-1)

            if gb.motionUp and gb.motionRight and col:
                if gb.display[ball.Ycor-1][ball.Xcor+1] != -1 and gb.display[ball.Ycor-1][ball.Xcor+1] != 8:
                    collision1 = collision.collision()
                    col = False
                    collision1.withTopRight(ball.Ycor-1, ball.Xcor+1)

            elif not(gb.motionUp) and not(gb.motionRight) and col:
                if gb.display[ball.Ycor+1][ball.Xcor-1] != -1 and gb.display[ball.Ycor+1][ball.Xcor-1] != 2019111026 and gb.display[ball.Ycor+1][ball.Xcor-1] != 8:
                    collision1 = collision.collision()
                    col = False
                    collision1.withBottomLeft(ball.Ycor+1, ball.Xcor-1)

            elif not(gb.motionRight) and gb.motionUp and col:
                if gb.display[ball.Ycor-1][ball.Xcor-1] != -1 and gb.display[ball.Ycor-1][ball.Xcor-1] != -1:
                    collision1 = collision.collision()
                    col = False
                    collision1.withTopLeft(ball.Ycor-1, ball.Xcor-1)

            elif gb.motionRight and not(gb.motionUp) and col:
                if gb.display[ball.Ycor+1][ball.Xcor+1] != -1  and gb.display[ball.Ycor+1][ball.Xcor+1] != 2019111026 and gb.display[ball.Ycor+1][ball.Xcor+1] != 8:
                    collision1 = collision.collision()
                    col = False
                    collision1.withBottomRight(ball.Ycor+1, ball.Xcor+1)
        if not(col) and gb.sound:
            os.system("vlc --intf dummy ./Sounds/1.mp3 &" )

        # if gb.display[ball.Ycor - Yspeed][ball.Xcor -Xspeed] != 123 and gb.display[ball.Ycor + Yspeed][ball.Xcor +Xspeed] != 123:
            # gb.display[ball.Ycor][ball.Xcor] = 8011
        # else:
        gb.display[ball.Ycor - Yspeed][ball.Xcor - Xspeed] = -1
        gb.display[ball.Ycor][ball.Xcor] = 8011

    def renderDisplay(self, set):
        isBrick = False
        print("          lvl: ", gb.Current_lvl,  "         Lives: ", gb.lives,
              "        Score: ", gb.score, "        Time: ", gb.time, "      Shoot rem time:", 30 - (gb.time - gb.shoottime))

        for y in range(0, 36):
            x = 0
            print("|", end='')
            while x < 122:
                if gb.display[y][x] == -1:
                    print(' ', end='')
                    x += 1
                elif gb.display[y][x] == 2019111026:
                    if gb.shootingslider:
                        a = 0
                        while a < self.length:
                            print(colorama.Back.LIGHTRED_EX+' ', end='')
                            print(colorama.Style.RESET_ALL, end='')
                            x += 1
                            a += 1
                    else:
                        a = 0
                        while a < self.length:
                            print(colorama.Back.LIGHTWHITE_EX+' ', end='')
                            print(colorama.Style.RESET_ALL, end='')
                            x += 1
                            a += 1
                elif gb.display[y][x] == 8011:
                    if gb.thru:
                        print(colorama.Fore.LIGHTRED_EX+'\u2B24', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                    else:
                        print(colorama.Fore.LIGHTCYAN_EX+'\u2B24', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        x += 1
                elif gb.display[y][x] == 8:
                    print(colorama.Fore.LIGHTRED_EX+'▴', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 1
                elif gb.display[y][x] == 12305:
                    print('\U0001F525', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12303:
                    print('▲', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12302:
                    print('\U00002195', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12301:
                    print('\U00002194', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12304:
                    print('↯', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12306:
                    print('✋', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                elif gb.display[y][x] == 12307:
                    print('F', end='')
                    print(colorama.Style.RESET_ALL, end='')
                    x += 2
                else:

                    if gb.display[y][x] == 0:
                        isBrick = True
                        print(colorama.Back.YELLOW+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 1:
                        isBrick = True
                        print(colorama.Back.RED+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 2:
                        isBrick = True
                        print(colorama.Back.BLUE+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 4:
                        print(colorama.Back.MAGENTA+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 69:
                        isBrick = True
                        print(colorama.Back.LIGHTGREEN_EX+'____', end='')
                        print(colorama.Style.RESET_ALL, end='')
                        print(' ', end='')
                    elif gb.display[y][x] == 111:
                        isBrick = True
                        if gb.time % 3 == 0:
                            print(colorama.Back.YELLOW+'____', end='')
                            print(colorama.Style.RESET_ALL, end='')
                            print(' ', end='')
                        elif gb.time % 2 == 0:
                            print(colorama.Back.RED+'____', end='')
                            print(colorama.Style.RESET_ALL, end='')
                            print(' ', end='')
                        else:
                            print(colorama.Back.BLUE+'____', end='')
                            print(colorama.Style.RESET_ALL, end='')
                            print(' ', end='')

                    print(colorama.Style.RESET_ALL, end='')
                    x += 5
                # print(x)
                if y == 34 and x < 122:
                    if gb.display[y][x] == 0 or gb.display[y][x] == 1 or gb.display[y][x] == 2 or gb.display[y][x] == 3 or gb.display[y][x] == 4 or gb.display[y][x] == 69:
                        print("F")
                        sys.exit()
            print('|\n', end='')

        if not(isBrick):
            if not(gb.lvlupkeypress):
                self.lvlup()
            gb.lvlupkeypress == False

        if gb.shootingslider:
            if gb.time%2:
                self.sliderShoot(set)
        self.moveBulletUp()
