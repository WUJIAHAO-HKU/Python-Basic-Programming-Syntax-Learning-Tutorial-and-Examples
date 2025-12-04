import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("大鱼吃小鱼")

# 定义颜色
white = (255, 255, 255)  # 背景色
black = (0, 0, 0)       # 文本色
red = (255, 0, 0)       # 敌方鱼颜色
blue = (0, 0, 255)      # 玩家鱼颜色

# 玩家鱼类
class PlayerFish:
    def __init__(self):
        # 创建玩家鱼的图像和初始位置
        self.image = pygame.Surface((50, 30))  # 玩家鱼大小：50x30
        self.image.fill(blue)                  # 填充蓝色
        self.rect = self.image.get_rect()      # 获取矩形区域
        self.rect.center = (width // 2, height // 2)  # 初始位置居中
        self.speed = 5                         # 移动速度
        self.score = 0                         # 初始分数

    def move(self, dx, dy):
        # 根据输入方向移动玩家鱼
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        # 边界检查，防止鱼超出屏幕
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

    def eat(self, fish):
        # 检查是否吃到敌方鱼
        if self.rect.colliderect(fish.rect):
            self.score += 1  # 增加分数
            return True      # 表示吃到了鱼
        return False

# 敌方鱼类
class EnemyFish:
    def __init__(self):
        # 创建敌方鱼的图像和初始位置
        self.image = pygame.Surface((30, 20))  # 敌方鱼大小：30x20
        self.image.fill(red)                   # 填充红色
        self.rect = self.image.get_rect()      # 获取矩形区域
        # 随机生成初始位置
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(0, height - self.rect.height)
        # 随机生成移动速度和方向
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])

    def move(self):
        # 敌方鱼自动移动
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # 边界检查，碰到边界反弹
        if self.rect.left < 0 or self.rect.right > width:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed_y *= -1

# 主游戏循环
def main():
    clock = pygame.time.Clock()  # 控制游戏帧率
    player = PlayerFish()        # 创建玩家鱼对象
    enemies = [EnemyFish() for _ in range(5)]  # 创建5条敌方鱼

    running = True
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击关闭按钮退出游戏
                running = False

        # 获取键盘输入并移动玩家鱼
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
        player.move(dx, dy)

        # 更新敌方鱼位置并检查是否被吃
        for enemy in enemies[:]:  # 使用切片避免修改列表时的错误
            enemy.move()
            if player.eat(enemy):
                enemies.remove(enemy)      # 移除被吃的鱼
                enemies.append(EnemyFish())  # 添加一条新鱼

        # 绘制游戏画面
        screen.fill(white)  # 填充背景
        screen.blit(player.image, player.rect)  # 绘制玩家鱼
        for enemy in enemies:
            screen.blit(enemy.image, enemy.rect)  # 绘制敌方鱼

        # 显示分数
        font = pygame.font.Font(None, 36)  # 设置字体大小
        text = font.render(f"Score: {player.score}", True, black)  # 渲染分数文本
        screen.blit(text, (10, 10))  # 显示在屏幕左上角

        pygame.display.flip()  # 更新屏幕显示
        clock.tick(60)        # 控制帧率为60FPS

    pygame.quit()  # 退出 Pygame

# 运行游戏
if __name__ == "__main__":
    main()
