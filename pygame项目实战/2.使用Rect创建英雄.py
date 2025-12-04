import pygame
hero_rect = pygame.Rect(100, 500, 120, 125) # 创建一个矩形对象
print("英雄的原点为：%d %d"%(hero_rect.x, hero_rect.y))
print("英雄的尺寸为：%d %d"%(hero_rect.width, hero_rect.height))
print("英雄的尺寸为：%d %d"% hero_rect.size)