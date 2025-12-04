import pygame

pygame.init() # 初始化pygame

# 创建窗口
screen = pygame.display.set_mode((480, 700)) # 设置窗口大小
pygame.display.set_caption("游戏窗口") # 设置窗口标题

# 绘制窗口背景
# 1. 加载图像数据
bg = pygame.image.load("pygame项目实战/images/background.png") # 加载背景图像
# 2. blit 绘制图像
screen.blit(bg, (0, 0)) # 将背景图像绘制到窗口上，坐标为(0, 0)
# 3. update 更新图像显示
#pygame.display.update() # 更新窗口显示

# 绘制英雄的飞机
hero = pygame.image.load("pygame项目实战/images/me1.png") # 加载英雄飞机图像
screen.blit(hero, (200, 500)) # 将英雄飞机图像绘制到窗口上，坐标为(200, 500)

#可以在所有绘制完成后再统一更新窗口显示
pygame.display.update() # 更新窗口显示  

while True:
    exit = input("是否退出游戏？(y/n): ") # 提示用户输入
    if exit == 'y': # 如果用户输入y，则退出游戏
        break # 退出循环

pygame.quit() # 退出pygame
