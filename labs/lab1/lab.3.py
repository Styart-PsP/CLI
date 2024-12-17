array = list(map(int, input("введіть елементи масиву ").split()))
negative_elements = [x for x in array if x < 0]
if negative_elements:
    max_negative = max(negative_elements)
    print(f"максимальний від'ємний елемент {max_negative}")
else:
    print("від'ємних елементів немає")
even_elements = [x for x in array if x % 2 == 0]
if even_elements:
    average_even = sum(even_elements) / len(even_elements)
    print(f"середнє арифметичне парних елементів: {average_even}")
else:
    print("парних елементів немає.")
non_zero_elements = [x for x in array if x != 0]
if non_zero_elements:
    print("ненульові елементи у зворотному порядку:", non_zero_elements[::-1])
else:
    print("Ненульових елементів немає.")