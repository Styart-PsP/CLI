import os
import sys
import subprocess

LABS_DIR = "labs"

def list_labs():
    if not os.path.exists(LABS_DIR):
        print("Папка з лабораторними роботами не знайдена!")
        return

    labs = [
        folder for folder in os.listdir(LABS_DIR)
        if os.path.isdir(os.path.join(LABS_DIR, folder)) and folder.startswith("lab")
    ]

    if not labs:
        print("Лабораторних робіт не знайдено.")
        return

    print("Доступні лабораторні роботи:")
    for idx, lab in enumerate(sorted(labs), start=1):
        lab_path = os.path.join(LABS_DIR, lab, "README.md")
        description = "Виконана успішно"
        if os.path.exists(lab_path):
            with open(lab_path, "r", encoding="utf-8") as f:
                description = f.readline().strip()
        print(f"{idx}. {lab} - {description}")


def run_lab(lab_number):
    lab_folder = f"lab{lab_number}"
    lab_path = os.path.join(LABS_DIR, lab_folder, f"{lab_folder}.py")

    if not os.path.exists(lab_path):
        print(f"Лабораторна робота {lab_number} не знайдена.")
        return

    print(f"Запуск лабораторної роботи {lab_number}...")
    try:
        subprocess.run(["python", lab_path], check=True)
        print(f"Лабораторна робота {lab_number} завершена успішно!")
    except subprocess.CalledProcessError:
        print(f"Помилка під час виконання лабораторної роботи {lab_number}.")


def print_help():
    print("Доступні команди:")
    print("  list                 - Показати список усіх лабораторних робіт.")
    print("  run <lab_number>     - Запустити обрану лабораторну роботу.")
    print("  help                 - Показати довідку.")
    print("  exit                 - Вийти з програми.")


def main():
    if len(sys.argv) < 2:
        print("Помилка: відсутня команда.\n")
        print_help()
        return

    command = sys.argv[1]

    if command == "list":
        list_labs()
    elif command == "run":
        if len(sys.argv) < 3:
            print("Помилка: не вказано номер лабораторної роботи.")
        else:
            run_lab(sys.argv[2])
    elif command in ("help", "--help", "-h"):
        print_help()
    else:
        print(f"Невідома команда: {command}")
        print_help()


if __name__ == "__main__":
    main()
