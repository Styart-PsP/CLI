import os

def create_group_file(group_name, students):

    file_name = f"{group_name}.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        for student, grade in students:
            f.write(f"{student},{grade:.2f}\n")
    print(f"Файл '{file_name}' створено.")

def read_group_file(group_name):

    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            data = f.readlines()
        return [line.strip().split(",") for line in data]
    else:
        print(f"Файл '{file_name}' не знайдено.")
        return []

def append_to_group_file(group_name, student, grade):

    file_name = f"{group_name}.txt"
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(f"{student},{grade:.2f}\n")
    print(f"Дані про студента '{student}' додано до файлу '{file_name}'.")

def search_files(directory="."):

    return [file for file in os.listdir(directory) if file.endswith(".txt")]

def search_data_in_file(group_name, student_name):

    data = read_group_file(group_name)
    for student, grade in data:
        if student == student_name:
            return student, float(grade)
    return None

def sort_group_file(group_name):

    data = read_group_file(group_name)
    sorted_data = sorted(data, key=lambda x: float(x[1]), reverse=True)
    file_name = f"{group_name}.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        for student, grade in sorted_data:
            f.write(f"{student},{float(grade):.2f}\n")
    print(f"Файл '{file_name}' відсортовано за середнім балом.")

students_group1 = [("Олександр", 85.5), ("Ірина", 92.0), ("Дмитро", 76.3)]
students_group2 = [("Анна", 88.5), ("Олег", 90.2), ("Марія", 79.5)]

create_group_file("group1", students_group1)
create_group_file("group2", students_group2)

append_to_group_file("group1", "Сергій", 80.0)
print(read_group_file("group1"))

print("Файли в каталозі:", search_files())
print("Пошук студента Ірина у групі group1:", search_data_in_file("group1", "Ірина"))

sort_group_file("group1")
print("Відсортовані дані групи group1:", read_group_file("group1"))