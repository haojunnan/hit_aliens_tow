#coding:gb2312
import pygame
from pygame.sprite import Sprite 
class Bullet(Sprite):
	"""�Էɴ��ӵ����й���"""
	def __init__(self,al_setting,rocket,screen):
		"""�ڷɴ�λ�ô���һ���ӵ�����"""
		super().__init__()
		self.screen = screen
		
		#��(0,0)�������ӵ������趨��ȷλ��
		self.rect = pygame.Rect(0,0,al_setting.bullet_width,
		al_setting.bullet_height)
		self.rect.x = rocket.rect.right
		self.rect.centery = rocket.rect.centery
		self.x = float(self.rect.x)
		self.centery = float(self.rect.centery)
		self.color = al_setting.bullet_color
		self.speed = al_setting.bullet_speed
	def update(self):
		"""�����ӵ�λ��"""
		self.x += self.speed
		self.rect.x = self.x
	def draw_bullet(self):
		"""����Ļ�ϻ����ӵ�"""
		pygame.draw.rect(self.screen,self.color,self.rect)
