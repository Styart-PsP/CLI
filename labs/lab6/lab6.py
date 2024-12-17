import requests
from bs4 import BeautifulSoup
from collections import Counter
import re


def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def analyze_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.get_text()
        words_count = word_frequency(text)

        tags = [tag.name for tag in soup.find_all()]
        tags_count = Counter(tags)

        links_count = len(soup.find_all('a'))
        images_count = len(soup.find_all('img'))

        print("=== Аналіз сторінки ===")
        print(f"URL: {url}")
        print("\n1. Топ 10 найчастіших слів:")
        for word, count in words_count.most_common(10):
            print(f"{word}: {count}")

        print("\n2. Частота HTML-тегів:")
        for tag, count in tags_count.items():
            print(f"{tag}: {count}")

        print(f"\n3. Кількість посилань: {links_count}")
        print(f"4. Кількість зображень: {images_count}")

    except requests.RequestException as e:
        print(f"Помилка при завантаженні сторінки: {e}")


if __name__ == "__main__":
    url = input("Введіть URL сторінки для аналізу: ")
    analyze_webpage(url)
