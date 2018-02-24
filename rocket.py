#coding:gb2312
import pygame
class Rocket():
	def __init__(self,al_setting,screen):
		"""�����ɻ���ͼ��λ��"""
		self.screen = screen
		self.al_setting = al_setting
		self.image = pygame.image.load('rocket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centery = self.screen_rect.centery
		self.rect.x = 0
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.x = float(self.rect.x)
		self.centery = float(self.rect.centery)
		self.rocket_speed = al_setting.rocket_speed
	def update(self):
		"""���·ɻ�λ��"""
		if self.moving_right and self.rect.right< self.screen_rect.right:
			self.x += self.rocket_speed
		elif self.moving_left and self.x > 0:
			self.x -= self.rocket_speed
		elif self.moving_up and self.rect.top> 0:
			self.centery -= self.rocket_speed
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.rocket_speed
		self.rect.x = self.x
		self.rect.centery = self.centery
	def blitem(self):
		"""���Ʒɴ�"""
		self.screen.blit(self.image,self.rect)
	
