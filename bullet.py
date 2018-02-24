#coding:gb2312
import pygame
from pygame.sprite import Sprite 
class Bullet(Sprite):
	"""对飞船子弹进行管理"""
	def __init__(self,al_setting,rocket,screen):
		"""在飞船位置创建一个子弹对象"""
		super().__init__()
		self.screen = screen
		
		#在(0,0)出绘制子弹，并设定正确位置
		self.rect = pygame.Rect(0,0,al_setting.bullet_width,
		al_setting.bullet_height)
		self.rect.x = rocket.rect.right
		self.rect.centery = rocket.rect.centery
		self.x = float(self.rect.x)
		self.centery = float(self.rect.centery)
		self.color = al_setting.bullet_color
		self.speed = al_setting.bullet_speed
	def update(self):
		"""更新子弹位置"""
		self.x += self.speed
		self.rect.x = self.x
	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)
