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
screen.blit(hero, (150, 300)) # 将英雄飞机图像绘制到窗口上，坐标为(200, 500)

#可以在所有绘制完成后再统一更新窗口显示
pygame.display.update() # 更新窗口显示  

#创建时钟对象
clock = pygame.time.Clock() # 创建时钟对象，用于控制游戏循环的帧率

#定义rect对象记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126) # 创建矩形对象，记录飞机的位置和大小

#游戏循环 -->意味着游戏的正式开始
while True:
    #设置循环的频率
    clock.tick(60)

    #捕获事件
    event_list = pygame.event.get()
    if len(event_list)>0:
        print(event_list)

    #2.修改飞机的位置
    hero_rect.y -= 1 # 每次循环将飞机向上移动10个像素

    #判断飞机是否飞出屏幕
    if hero_rect.y <= -126: # 如果飞机的y坐标小于等于-126，则将飞机移到屏幕底部
        hero_rect.y = 700 # 将飞机的y坐标设置为700
    #3.调用blit方法绘制图像
    #每次循环都要先重绘制背景图像
    screen.blit(bg, (0, 0)) # 将背景图像绘制到窗口上，坐标为(0, 0)
    screen.blit(hero, hero_rect) # 将背景图像绘制到窗口上，坐标为(0, 0)

    #4.调用update方法更新图像显示
    pygame.display.update() # 更新窗口显示

pygame.quit() # 退出pygame
