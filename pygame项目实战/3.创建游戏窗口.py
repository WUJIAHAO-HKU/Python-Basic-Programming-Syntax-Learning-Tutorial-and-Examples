import pygame

pygame.init() # 初始化pygame

# 创建窗口
screen = pygame.display.set_mode((480, 700)) # 设置窗口大小

while True:

    exit = input("是否退出游戏？(y/n): ") # 提示用户输入
    if exit == 'y': # 如果用户输入y，则退出游戏
        break # 退出循环

pygame.quit() # 退出pygame
