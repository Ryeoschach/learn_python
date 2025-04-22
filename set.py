
# 集合是一种无序的集合，可以包含任意类型的唯一元素。
# 集合中的元素是唯一的，不能重复。
# 集合是可变的，但集合中的元素必须是不可变的。
# 集合元素用 "{}" 包裹


my_fruits = {"苹果", "香蕉", "橙子", "草莓"}

friend_fruits = {"香蕉", "西瓜", "草莓", "蓝莓"}

# 使用 ^ 符号
symmetric_difference_fruits = my_fruits ^ friend_fruits
print(f"我们之间不同的水果 (对称差集): {symmetric_difference_fruits}")
# 输出: 我们之间不同的水果 (对称差集): {'苹果', '橙子', '西瓜', '蓝莓'}

# 使用 symmetric_difference() 方法
another_symmetric_difference_fruits = my_fruits.symmetric_difference(friend_fruits)
print(f"我们之间不同的水果 (对称差集 - 方法): {another_symmetric_difference_fruits}")
# 输出: 我们之间不同的水果 (对称差集 - 方法): {'苹果', '橙子', '西瓜', '蓝莓'}
