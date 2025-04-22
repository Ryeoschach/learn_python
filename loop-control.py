import random  # 导入 random 模块，用于生成随机数

def guess_number():
    """实现猜数字游戏的功能"""
    secret_number = random.randint(1, 100)  # 生成 1 到 100 之间的随机整数作为秘密数字
    attempts = 0  # 初始化尝试次数为 0
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1 到 100 之间的整数，你来猜猜看是多少。")

    while True:  # 进入无限循环，直到玩家猜对为止
        try:
            guess = int(input("请输入你的猜测："))  # 提示用户输入猜测的数字，并尝试转换为整数
            attempts += 1  # 每次猜测后，尝试次数加 1
            if guess < secret_number:
                print("太小了！再试一次。")  # 如果猜测的数字小于秘密数字，给出提示
            elif guess > secret_number:
                print("太大了！再试一次。")  # 如果猜测的数字大于秘密数字，给出提示
            else:
                print(f"恭喜你，猜对了！答案就是 {secret_number}。")  # 如果猜测的数字等于秘密数字，给出恭喜信息
                print(f"你一共尝试了 {attempts} 次。")  # 显示玩家尝试的次数
                break  # 猜对后，使用 break 语句跳出 while 循环
        except ValueError:
            print("输入无效，请输入一个整数。")  # 如果用户输入的不是整数，捕获 ValueError 异常并给出提示

if __name__ == "__main__":
    guess_number()  # 当直接运行此脚本时，调用 guess_number() 函数开始游戏