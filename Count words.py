from collections import Counter
import re

# Ваш текст (замените эту строку на ваш текст)
text = """
Ваш текст здесь
"""

# Разделите текст на слова с помощью регулярного выражения
words = re.findall(r'\w+', text.lower())

# Подсчет частотности слов
word_counts = Counter(words)

# Вывод топ 30 слов и их частотности
print("Word - Count Mention")
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"{word} - {count}")
