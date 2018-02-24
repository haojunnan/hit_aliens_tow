#coding:gb2312
import sys
import pygame
from bullet import Bullet
def key_down(event,rocket,al_setting,screen,bullets):
	"""对应按键激活移动"""
	if event.key == pygame.K_RIGHT:
		rocket.moving_right = True
	elif event.key == pygame.K_LEFT:
		rocket.moving_left = True
	elif event.key == pygame.K_UP:
		rocket.moving_up = True
	elif event.key == pygame.K_DOWN:
		rocket.moving_down = True
	elif event.key == pygame.K_SPACE:
		if len(bullets) < al_setting.bullet_num:
			new_bullet = Bullet(al_setting,rocket,screen)
			bullets.add(new_bullet)
def key_up(event,rocket):
	if event.key == pygame.K_RIGHT:
		rocket.moving_right = False
	elif event.key == pygame.K_LEFT:
		rocket.moving_left = False
	elif event.key == pygame.K_UP:
		rocket.moving_up = False
	elif event.key == pygame.K_DOWN:
		rocket.moving_down = False
def check_events(rocket,al_setting,screen,bullets):
	"""鼠标响应事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			key_down(event,rocket,al_setting,screen,bullets)
		elif event.type == pygame.KEYUP:
			key_up(event,rocket)
def update_screen(al_setting,screen,rocket,bullets):
	"""刷新界面"""
	screen.fill(al_setting.screen_color)
	for bullet in bullets:
		bullet.draw_bullet()
	rocket.blitem()
	pygame.display.flip()
def update_bullets(bullets,al_setting):
	"""更新子弹库，消除多余子弹"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.x > al_setting.screen_width:
			bullets.remove(bullet)
