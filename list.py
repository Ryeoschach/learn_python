import sys

def print_header(title):
    """打印格式化的标题"""
    print(f"\n{'=' * 20} {title} {'=' * 20}\n")

def calculate_allocated(lst):
    """
    计算列表实际分配的元素容量 (可容纳的元素数量)

    原理说明:
    1. lst.__sizeof__() 返回列表对象占用的总字节数
    2. [].__sizeof__() 返回空列表占用的字节数 (列表对象的基本开销)
    3. 两者之差为存储元素引用的内存空间
    4. 在64位系统上,每个元素引用占8字节,所以除以8得到容量

    注意: 这个容量可能大于实际元素数量,因为Python会预分配空间
    """
    return (lst.__sizeof__() - [].__sizeof__()) // 8

# =========================== 验证扩容发生的时刻 ===========================
print_header("1. 验证 Python 列表扩容时刻")
print("理论上,Python 列表的扩容序列应该是 0, 4, 8, 16, 24, 32, 40, 52...")
print("这个序列遵循公式: ((newsize + (newsize >> 3) + 6) & ~3)")
print("其中,newsize是需要的元素数量,>>是位运算右移,&~3表示向下取整到4的倍数")
print("简单理解就是: 大致增加当前大小的1/8,再加上6,然后调整为4的倍数")

lst = []
last_allocated = 0
expansion_points = []

# 逐步添加元素,记录发生扩容的时刻
for i in range(100):
    lst.append(i)
    current_allocated = calculate_allocated(lst)

    # 如果容量增加了,说明发生了扩容
    if current_allocated > last_allocated:
        expansion_points.append((i + 1, current_allocated))
        last_allocated = current_allocated

print("\n扩容发生在以下位置 (元素数量,新容量):")
for point in expansion_points:
    print(f"  当添加第 {point[0]} 个元素时,容量扩展到 {point[1]}")

# =========================== 总结 ===========================
print_header("2. 总结")
print("1. Python 列表扩容遵循的序列: ", [point[1] for point in expansion_points])
print("2. 扩容策略使用公式: ((newsize + (newsize >> 3) + 6) & ~3)")
print("   - 这相当于增加约12.5%的容量,再加上固定值,并四字节对齐")
print("3. 这种机制减少了频繁的内存重新分配,提高了列表操作的性能")
print("4. 列表不会自动缩小容量,即使删除大量元素,已分配的内存仍然保留")
print("5. 这种策略在时间效率和空间效率之间取得平衡")

# =========================== 不同创建方式的内存分配 ===========================
print_header("3. 不同创建方式的内存分配")
print("Python提供多种创建列表的方式,它们在内存分配上可能有细微差别")

creation_methods = [
    ("直接创建", [1, 1, 1]),  # 使用直接字面量创建
    ("乘法创建", [1] * 3),  # 使用重复操作符创建
    ("列表推导", [1 for _ in range(3)]),  # 使用列表推导式创建
    ("range转换", list(range(3))),  # 从其他可迭代对象转换
]

print("\n初始内存分配:")
print("不同创建方式可能导致不同的初始容量分配")
for name, lst in creation_methods:
    size = len(lst)
    allocated = calculate_allocated(lst)
    memory = sys.getsizeof(lst)
    print(f"  {name}: 元素数量={size}, 容量={allocated}, 内存={memory}字节")
    # 计算空间利用率
    utilization = (size / allocated * 100) if allocated else 0
    print(f"    - 空间利用率: {utilization:.1f}%")

print("\n添加一个元素后:")
print("添加元素可能触发扩容,根据初始容量的不同,扩容行为也可能不同")
for name, lst in creation_methods:
    before_size = len(lst)
    before_allocated = calculate_allocated(lst)
    before_memory = sys.getsizeof(lst)

    # 添加一个元素
    lst.append(1)

    after_size = len(lst)
    after_allocated = calculate_allocated(lst)
    after_memory = sys.getsizeof(lst)

    # 计算详细变化
    size_change = after_size - before_size
    capacity_change = after_allocated - before_allocated
    memory_change = after_memory - before_memory

    print(f"  {name}:")
    print(f"    - 元素数量: {before_size} → {after_size} (+{size_change})")
    print(f"    - 容量: {before_allocated} → {after_allocated} (+{capacity_change})")
    print(f"    - 内存: {before_memory} → {after_memory} (+{memory_change}字节)")

    # 是否发生扩容
    if capacity_change > 0:
        print(
            f"    - 发生扩容! 新容量为旧容量的 {after_allocated / before_allocated:.2f} 倍"
        )
    else:
        print("    - 未发生扩容,当前容量足够容纳新元素")

    # 空间利用率
    utilization = after_size / after_allocated * 100
    print(f"    - 当前空间利用率: {utilization:.1f}%")

# =========================== 缩容行为测试 ===========================
print_header("4. 列表缩容行为测试")
print("Python列表在删除元素时的缩容行为")

# 创建一个大列表
big_list = list(range(100))
initial_size = len(big_list)
initial_allocated = calculate_allocated(big_list)
initial_memory = sys.getsizeof(big_list)

print(f"初始列表: 元素数量={initial_size}, 容量={initial_allocated}, 内存={initial_memory}字节")

# 测试删除元素后的容量变化
test_points = [90, 60, 55, 50, 40, 30, 20, 10, 5, 0]
results = []

print("\n逐步删除元素测试:")
for remain_size in test_points:
    # 从原始列表创建副本以确保每次测试的起点相同
    test_list = big_list.copy()
    
    # 删除元素
    del test_list[remain_size:]
    
    # 测量关键指标
    size = len(test_list)
    allocated = calculate_allocated(test_list)
    memory = sys.getsizeof(test_list)
    
    # 存储结果
    results.append((size, allocated, memory))
    
    print(f"  保留 {remain_size} 个元素:")
    print(f"    - 元素数量: {size} (削减了 {initial_size - size} 个)")
    print(f"    - 容量: {allocated} (与初始值相比变化: {allocated - initial_allocated})")
    print(f"    - 内存: {memory} 字节")

# 比较结果，检查是否有缩容发生
print("\n缩容行为分析:")
shrink_points = []
for i in range(1, len(results)):
    prev = results[i-1]
    curr = results[i]
    if curr[1] < prev[1]:  # 检查容量是否减少
        shrink_points.append((test_points[i-1], test_points[i]))
        print(f"  检测到缩容: 从保留 {test_points[i-1]} 个元素到 {test_points[i]} 个元素时")
        print(f"    - 容量 {prev[1]} -> {curr[1]}")

if not shrink_points:
    print("  未检测到自动缩容行为，Python 列表不会随元素删除自动释放内存")

# 测试几种手动缩容方法
print("\n手动缩容方法比较:")

# 方法1: copy()
test_list = big_list.copy()
del test_list[10:]  # 删除大部分元素，保留10个
copy_list = test_list.copy()
print("1. 使用 list.copy() 方法:")
print(f"  - 删除后: 元素={len(test_list)}, 容量={calculate_allocated(test_list)}, 内存={sys.getsizeof(test_list)}字节")
print(f"  - 复制后: 元素={len(copy_list)}, 容量={calculate_allocated(copy_list)}, 内存={sys.getsizeof(copy_list)}字节")

# 方法2: 切片
test_list = big_list.copy()
del test_list[10:]  # 同样删除保留10个
slice_list = test_list[:]
print("2. 使用切片 list[:] 操作:")
print(f"  - 删除后: 元素={len(test_list)}, 容量={calculate_allocated(test_list)}, 内存={sys.getsizeof(test_list)}字节")
print(f"  - 切片后: 元素={len(slice_list)}, 容量={calculate_allocated(slice_list)}, 内存={sys.getsizeof(slice_list)}字节")

# 方法3: list()构造函数
test_list = big_list.copy()
del test_list[10:]  # 同样删除保留10个
new_list = list(test_list)
print("3. 使用 list() 构造函数:")
print(f"  - 删除后: 元素={len(test_list)}, 容量={calculate_allocated(test_list)}, 内存={sys.getsizeof(test_list)}字节")
print(f"  - 构造后: 元素={len(new_list)}, 容量={calculate_allocated(new_list)}, 内存={sys.getsizeof(new_list)}字节")

# =========================== 说明和结论 ===========================
print_header("5. 总体结论")
print("1. Python列表是动态数组，会根据需要自动调整容量")
print("2. 扩容策略: 新容量 ≈ 当前大小 + 当前大小/8 + 6 (取4的倍数)")
print("3. 不同创建方式可能有不同的初始容量分配")
print("4. 列表在特定条件下会自动缩容:")
print("   - 当元素数量降至容量的约50%以下时，会触发缩容")
print("   - 缩容后的容量通常为之前的50%-60%左右")
print("5. 手动缩容的有效方法包括:")
print("   - copy()、切片操作、list()构造函数")
print("6. 这种内存管理策略平衡了时间和空间效率:")
print("   - 避免频繁的内存分配/释放操作(时间效率)")
print("   - 在元素数量大幅减少时释放内存(空间效率)")