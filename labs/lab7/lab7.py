import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import re


def task1_plot_function():
    x = np.linspace(0.1, 4, 500)
    y = 10 * np.cos(x ** 2) / x ** 2

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Y(x) = 10 * cos(x^2) / x^2', color='blue')
    plt.title("Графік функції Y(x) = 10 * cos(x^2) / x^2")
    plt.xlabel("x")
    plt.ylabel("Y(x)")
    plt.grid()
    plt.legend()
    plt.savefig("task1_function_plot.png")
    print("Завдання 1: Графік функції збережено як 'task1_function_plot.png'.")


def task2_letter_histogram(text):
    letters = re.findall(r'[a-zA-Zа-яА-ЯіІєЄїЇ]', text)
    letter_counts = Counter(letters)

    plt.figure(figsize=(8, 6))
    plt.bar(letter_counts.keys(), letter_counts.values(), color='orange')
    plt.title("Гістограма частоти появи літер")
    plt.xlabel("Літери")
    plt.ylabel("Частота")
    plt.grid(axis='y')
    plt.savefig("task2_letter_histogram.png")  # Зберігаємо у файл
    print("Завдання 2: Гістограму літер збережено як 'task2_letter_histogram.png'.")


def task3_sentence_histogram(text):
    normal_sentences = re.findall(r'[^.!?]+[.]', text)
    question_sentences = re.findall(r'[^.!?]+[?]', text)
    exclamatory_sentences = re.findall(r'[^.!?]+[!]', text)
    ellipsis_sentences = re.findall(r'[^.!?]+\.\.\.', text)

    sentence_counts = {
        "Звичайні": len(normal_sentences),
        "Питальні": len(question_sentences),
        "Окличні": len(exclamatory_sentences),
        "З трикрапкою": len(ellipsis_sentences)
    }

    plt.figure(figsize=(8, 6))
    plt.bar(sentence_counts.keys(), sentence_counts.values(), color='green')
    plt.title("Гістограма типів речень у тексті")
    plt.xlabel("Типи речень")
    plt.ylabel("Кількість")
    plt.grid(axis='y')
    plt.savefig("task3_sentence_histogram.png")
    print("Завдання 3: Гістограму типів речень збережено як 'task3_sentence_histogram.png'.")


# Основна функція
if __name__ == "__main__":
    # Завдання 1
    task1_plot_function()

    # Завдання 2
    sample_text = """
    Програмування на Python є цікавим. Python дуже зручний для наукових розрахунків і обробки даних.
    А як щодо побудови графіків? Це легко!
    """
    task2_letter_histogram(sample_text)

    # Завдання 3
    task3_sentence_histogram(sample_text)
