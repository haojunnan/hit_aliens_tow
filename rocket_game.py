#coding:gb2312
import pygame
import sys
from rocket import Rocket
from pygame.sprite import Group
from test_setting import Test_Setting 
import game_functions as gm
def run_game():
	pygame.init()
	al_setting = Test_Setting()
	screen = pygame.display.set_mode((al_setting.screen_width,
	al_setting.screen_height))
	pygame.display.set_caption('ready go')
	rocket = Rocket(al_setting,screen)
	bullets = Group()
	while True:
		gm.check_events(rocket,al_setting,screen,bullets)
		rocket.update()
		gm.update_bullets(bullets,al_setting)
		gm.update_screen(al_setting,screen,rocket,bullets)
run_game()
