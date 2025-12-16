import os

def create_test_files():
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write("I love Python programming.\nPython is great.\nJava is also cool.\n")
    
    with open("old_version.txt", "w", encoding="utf-8") as f:
        f.write("Line 1: Hello\nLine 2: World\nLine 3: Python\n")
    
    with open("new_version.txt", "w", encoding="utf-8") as f:
        f.write("Line 1: Hello\nLine 2: World Revised\nLine 3: Python\n")
        
    with open("source.txt", "w", encoding="utf-8") as f:
        f.write("This text contains badword1 and badword2 inside.\nDo not use badword1.")
        
    with open("words.txt", "w", encoding="utf-8") as f:
        f.write("badword1 badword2")

create_test_files()
print("Тестовые файлы созданы!\n")


# --- ЗАДАНИЕ 1 ---
print(">>> ЗАДАНИЕ 1: Замена слов")
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace("Python", "Java")

with open("data.txt", "w", encoding="utf-8") as f:
    f.write(new_content)
print("Слова заменены. Проверьте data.txt\n")


# --- ЗАДАНИЕ 2 ---
print(">>> ЗАДАНИЕ 2: Подсчет символов")
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("char_count.txt", "w", encoding="utf-8") as f:
    for line in lines:
        count = len(line.strip())
        f.write(f"Рядок: {count} символів\n")
print("Статистика сохранена в char_count.txt\n")


# --- ЗАДАНИЕ 3 ---
print(">>> ЗАДАНИЕ 3: Разница файлов")
with open("old_version.txt", "r", encoding="utf-8") as f1, \
     open("new_version.txt", "r", encoding="utf-8") as f2:
    set_old = set(f1.readlines())
    set_new = set(f2.readlines())

diff = set_old.symmetric_difference(set_new)

with open("differences.txt", "w", encoding="utf-8") as f:
    for line in diff:
        f.write(line)
print("Различия записаны в differences.txt\n")


# --- ЗАДАНИЕ 4 ---
print(">>> ЗАДАНИЕ 4: Цензура")

with open("words.txt", "r", encoding="utf-8") as f:
    forbidden_words = f.read().split()

with open("source.txt", "r", encoding="utf-8") as f:
    text = f.read()

for word in forbidden_words:
    text = text.replace(word, "***")

with open("censored.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Текст отцензурирован в censored.txt\n")