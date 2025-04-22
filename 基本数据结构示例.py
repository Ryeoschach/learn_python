"""
Python 基本数据结构演示 - 图书管理系统

本示例展示了如何使用 Python 的核心数据结构：
- 列表（List）：有序、可变、允许重复元素
- 元组（Tuple）：有序、不可变、允许重复元素
- 字典（Dictionary）：键值对、可变、键唯一
- 集合（Set）：无序、可变、元素唯一
"""

# ==================== 字典（Dictionary）示例 ====================
print("\n===== 字典（Dictionary）示例 =====")
print("字典用于存储键值对，通过键快速访问值")

# 使用字典存储图书信息（ISBN (国际标准书号)-> (书名, 作者, 出版年份)）
books = {
    "978-957-33-3357-9": ("百年孤独", "加夫列尔·加西亚·马尔克斯", 1967),
    "978-7-5366-9293-0": ("三体", "刘慈欣", 2008),
    "978-7-5308-6787-7": ("悲惨世界", "维克多·雨果", 1862),
    "999-9-9999-9999-9": ("法外狂徒", "张三", 2020),
    "978-1-4516-2380-7": ("时间简史", "史提芬·威廉·霍金", 1988),
}

# 字典基本操作演示
print("\n1. 访问字典元素:")
print(f"ISBN为978-7-5366-9293-0的书是: 《{books['978-7-5366-9293-0'][0]}》，作者是: {books['978-7-5366-9293-0'][1]}")

print("\n2. 添加/修改字典元素:")
books["978-7-5327-5027-9"] = ("动物农场", "乔治·奥威尔", 1945)
print(f"添加后的书籍数量: {len(books)}")

print("\n3. 遍历字典:")
for isbn, book_info in books.items():
    title, author, year = book_info
    print(f"《{title}》 - {author} ({year}年) [ISBN: {isbn}]")

print("\n4. 检查键是否存在:")
isbn_to_check = "978-0-451-52493-5"
if isbn_to_check in books:
    print(f"ISBN {isbn_to_check} 在书库中")
else:
    print(f"ISBN {isbn_to_check} 不在书库中")

print("\n5. 字典方法演示:")
print(f"所有ISBN: {list(books.keys())}")
print(f"第一本书的信息: {list(books.values())[0]}")
print(f"获取ISBN为'978-7-5366-9293-0'的信息，若不存在返回'未知': {books.get('978-7-5366-9293-0', '未知')}")
print(f"获取ISBN为'978-0-451-52493-5'的信息，若不存在返回'未知': {books.get('978-0-451-52493-5', '未知')}")

# 创建一个通过书名查找ISBN的辅助字典
title_to_isbn = {book_info[0]: isbn for isbn, book_info in books.items()}
print("\n6. 通过书名查找ISBN:")
book_name = "三体"
if book_name in title_to_isbn:
    print(f"《{book_name}》的ISBN是: {title_to_isbn[book_name]}")
else:
    print(f"《{book_name}》不在书库中")

# ==================== 列表（List）示例 ====================
print("\n\n===== 列表（List）示例 =====")
print("列表用于存储有序集合，元素可以修改和重复")

# 使用列表存储借阅记录（每条记录包含用户名、ISBN、日期）
# 注意：现在使用ISBN代替书名
borrow_records = [
    ["张三", "978-957-33-3357-9", "2025-03-01", "2025-03-15"],  # [用户, ISBN, 借阅日期, 归还日期]
    ["李四", "978-7-5366-9293-0", "2025-03-05", None],
    ["李四", "978-7-5308-6787-7", "2025-03-10", None],
    ["王五", "978-7-5327-5027-9", "2025-03-12", "2025-03-20"],
]

# 列表基本操作演示
print("\n1. 访问列表元素:")
isbn = borrow_records[0][1]
book_title = books[isbn][0]
print(f"第一条借阅记录: {borrow_records[0][0]} 借阅了《{book_title}》")

print(f"第二条记录的ISBN: {borrow_records[1][1]}")
print(f"最后一条记录: {borrow_records[-1]}")

print("\n2. 切片操作:")
print(f"前两条记录: {borrow_records[:2]}")
print(f"从第三条开始的记录: {borrow_records[2:]}")

print("\n3. 添加元素:")
borrow_records.append(["孙六", "978-7-5327-5027-9", "2025-03-22", None])
print(f"添加后的记录数量: {len(borrow_records)}")

print("\n4. 使用列表推导式:")
active_borrows = [record for record in borrow_records if record[3] is None]
print(f"当前未归还的借阅: {len(active_borrows)} 条")
for record in active_borrows:
    user, isbn, borrow_date, _ = record
    book_title = books[isbn][0]
    print(f"  {user} 借阅了 《{book_title}》 于 {borrow_date}")

print("\n5. 列表排序:")
# 按借阅日期排序
borrow_records.sort(key=lambda x: x[2])
print("按借阅日期排序后的前两条记录:")
for record in borrow_records[:2]:
    user, isbn, borrow_date, _ = record
    book_title = books[isbn][0]
    print(f"  {user} - 《{book_title}》 - {borrow_date}")

# ==================== 元组（Tuple）示例 ====================
print("\n\n===== 元组（Tuple）示例 =====")
print("元组是不可变的列表，创建后内容不能修改")

# 使用元组存储作者信息（固定不变的数据）
authors = (
    ("加夫列尔·加西亚·马尔克斯", "哥伦比亚", "1927-3-6", "2014-4-17"),  # (姓名, 国籍, 出生日期, 逝世日期)
    ("刘慈欣", "中国", "1963-6-23", None),
    ("维克多·雨果", "法国", "1802-2-26", "1885-5-22"),
    ("乔治·奥威尔", "英国", "1903-6-25", "1950-1-21"),
    ("张三", "未知", "2000-6-25", None),
    ("史提芬·威廉·霍金", "英国", "1942-1-8", "2018-3-14")
)

# 元组基本操作演示
print("\n1. 访问元组元素:")
print(f"第一位作者: {authors[0][0]}, 来自 {authors[0][1]}")

print("\n2. 元组不可修改:")
print("尝试修改元组会引发错误，比如: authors[0] = ('新作者', '新国籍', '出生日期', '逝世日期')")

print("\n3. 元组解包:")
name, country, birth, death = authors[1]
print(f"作者信息解包: {name} 是 {country} 作家，出生于 {birth}" + (f"，逝世于 {death}" if death else ""))

print("\n4. 在函数返回值中使用元组:")
def get_author_lifespan(author_tuple):
    """返回作者姓名和寿命"""
    name, _, birth, death = author_tuple
    if not death:
        return (name, "在世")
    birth_year = int(birth.split("-")[0])
    death_year = int(death.split("-")[0])
    return (name, death_year - birth_year)

for author in authors:
    name, lifespan = get_author_lifespan(author)
    print(f"  {name}: {lifespan}" + (" 岁" if isinstance(lifespan, int) else ""))

# ==================== 集合（Set）示例 ====================
print("\n\n===== 集合（Set）示例 =====")
print("集合存储唯一元素，无序，适合成员检测和消除重复")

# 使用集合存储已借出的图书ISBN和可借阅的图书ISBN
isbns_available = {"978-957-33-3357-9", "978-7-5327-5027-9", "978-1-4516-2380-7"}
isbns_borrowed = {"978-7-5366-9293-0", "978-957-33-3357-9", "978-7-5308-6787-7", "978-7-5327-5027-9"}

# 为了更好地显示，创建ISBN到书名的映射
isbn_to_title = {isbn: info[0] for isbn, info in books.items()}

# 集合基本操作演示
print("\n1. 集合运算:")
all_isbns = isbns_available | isbns_borrowed
all_titles = {isbn_to_title.get(isbn, f"未知书籍 ({isbn})") for isbn in all_isbns}
print(f"所有图书: {all_titles}")  # 并集

inconsistent_isbns = isbns_available & isbns_borrowed
inconsistent_titles = {isbn_to_title.get(isbn, f"未知书籍 ({isbn})") for isbn in inconsistent_isbns}
print(f"既在馆又已借出(数据不一致): {inconsistent_titles}")  # 交集

available_only = isbns_available - isbns_borrowed
available_titles = {isbn_to_title.get(isbn, f"未知书籍 ({isbn})") for isbn in available_only}
print(f"在馆但未借出: {available_titles}")  # 差集

exclusive_isbns = isbns_available ^ isbns_borrowed
exclusive_titles = {isbn_to_title.get(isbn, f"未知书籍 ({isbn})") for isbn in exclusive_isbns}
print(f"仅在其中一个集合的书: {exclusive_titles}")  # 对称差

print("\n2. 添加和删除元素:")
isbns_available.add("978-7-5366-9293-0")  # 添加三体的ISBN
isbns_borrowed.remove("978-7-5327-5027-9")  # 删除动物农场的ISBN
print(f"更新后馆内可借: {[isbn_to_title.get(isbn, f'未知书籍 ({isbn})') for isbn in isbns_available]}")
print(f"更新后已借出: {[isbn_to_title.get(isbn, f'未知书籍 ({isbn})') for isbn in isbns_borrowed]}")

print("\n3. 成员检测:")
isbn_to_check = "978-1-4516-2380-7"  # 假设是"时间简史"的ISBN
if isbn_to_check in isbns_available:
    print(f"ISBN {isbn_to_check} 对应的书可借阅")
else:
    print(f"ISBN {isbn_to_check} 对应的书不可借阅")

print("\n4. 集合推导式:")
long_isbn_books = {isbn for isbn in (isbns_available | isbns_borrowed) if isbn.count("-") > 3}
print(f"ISBN含有超过3个连字符的书: {[isbn_to_title.get(isbn, f'未知书籍 ({isbn})') for isbn in long_isbn_books]}")

# ==================== 数据结构组合使用 ====================
print("\n\n===== 数据结构组合使用 =====")

# 用户借阅信息统计
users = {
    "张三": {
        "已借": ["978-957-33-3357-9"], 
        "已还": ["978-1-4516-2380-7"]
    },
    "李四": {
        "已借": ["978-7-5366-9293-0", "978-7-5308-6787-7"], 
        "已还": []
    },
    "王五": {
        "已借": [], 
        "已还": ["978-7-5327-5027-9"]
    },
}

# 创建所有用户借过的书的集合
all_borrowed_isbns = set()
for user, records in users.items():
    # 集合的更新操作
    all_borrowed_isbns.update(records["已借"])
    all_borrowed_isbns.update(records["已还"])

all_borrowed_titles = [isbn_to_title.get(isbn, f"未知书籍 ({isbn})") for isbn in all_borrowed_isbns]
print(f"所有被借阅过的图书: {all_borrowed_titles}")

# 统计每本书被借阅的次数
book_borrow_count = {}
for user, records in users.items():
    for isbn in records["已借"] + records["已还"]:
        if isbn in book_borrow_count:
            book_borrow_count[isbn] += 1
        else:
            book_borrow_count[isbn] = 1

# 按借阅次数排序（转换为列表进行排序）
sorted_isbns = sorted(book_borrow_count.items(), key=lambda x: x[1], reverse=True)
print("\n借阅次数排行:")
for isbn, count in sorted_isbns:
    title = isbn_to_title.get(isbn, f"未知书籍 ({isbn})")
    print(f"  《{title}》: {count} 次")

print("\n各用户借阅情况:")
for user, records in users.items():
    total_borrowed = len(records["已借"]) + len(records["已还"])
    currently_borrowed = len(records["已借"])
    print(f"  {user}: 总计借阅 {total_borrowed} 本，当前借阅 {currently_borrowed} 本")

# ==================== 元组的修改 ====================
print("\n\n===== 数据结构更新作者的去世时间组合使用 =====")
# 获取原始作者信息
def update_author_death(authors, author_name, death_date):
    """更新作者的出生日期，返回新的作者元组集合"""
    new_authors = []
    for author in authors:
        name, country, birth, death = author
        if name == author_name:
            # 替换为更新后的作者信息
            new_authors.append((name, country, birth, death_date))
        else:
            # 保持原来的信息不变
            new_authors.append(author)
    return tuple(new_authors)

# 使用函数更新作者信息
print("\n更新前的作者信息:")
for author in authors:
    print(f"  {author[0]}: {'在世' if author[3] is None else '逝世于 ' + author[3]}")

# 假设张三逝世（仅用于演示）
authors = update_author_death(authors, "张三", "2030-1-1")

print("\n更新后的作者信息:")
for author in authors:
    print(f"  {author[0]}: {'在世' if author[3] is None else '逝世于 ' + author[3]}")