from collections import Counter

emotion_words = {
    "joy": ["радість", "щастя", "сміх", "усмішка", "задоволення", "щасливий", "захват", "радісно", "веселощі",
            "щасливий"],
    "sadness": ["смуток", "печаль", "сум", "гіркота", "сумно", "страждання", "скорбота", "розчарування", "жаль",
                "депресія"],
    "fear": ["страх", "жах", "переляк", "тривога", "паніка", "страшно", "ляк", "нервозність", "жахливо", "боятися"]
}

text = """
Ваш текст тут...
"""


def analyze_emotions(text, emotion_words):
    words = text.lower().split()

    emotion_counts = {emotion: 0 for emotion in emotion_words}

    for emotion, words_list in emotion_words.items():
        counter = Counter(word for word in words if word in words_list)
        emotion_counts[emotion] = sum(counter.values())

    return emotion_counts


emotion_counts = analyze_emotions(text, emotion_words)

print("Частота слів для кожної емоції:")
for emotion, count in emotion_counts.items():
    print(f"{emotion}: {count}")

dominant_emotion = max(emotion_counts, key=emotion_counts.get)
print(f"\nПереважаюча емоція: {dominant_emotion}")