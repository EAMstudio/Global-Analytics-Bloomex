from collections import Counter
import re

def analyze_text(text):
    # Split the text into words using a regular expression
    words = re.findall(r'\w+', text.lower())

    # Count word frequency
    word_counts = Counter(words)

    # Print the top 30 words and their frequencies
    print("Word - Count Mention")
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:30]:
        print(f"{word} - {count}")

# Text here
text = """
Александр Пушкин
Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.
"""

# Call the function with your text
analyze_text(text)
