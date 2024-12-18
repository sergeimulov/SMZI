import os
import matplotlib.pyplot as plt

def count_spaces(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return text.count(' ')
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None

def plot_space_comparison(file1, file2):
    spaces_file1 = count_spaces(file1)
    spaces_file2 = count_spaces(file2)

    if spaces_file1 is not None and spaces_file2 is not None:
        labels = [os.path.basename(file1), os.path.basename(file2)]
        values = [spaces_file1, spaces_file2]

        plt.bar(labels, values, color=['blue', 'orange'])
        plt.ylabel('Количество пробелов')
        plt.title('Сравнение количества пробелов в двух файлах')
        plt.show()

def main():
    DATA_DIR = "D:\\study\\STEGO3"  # Замените на вашу директорию
    file1_path = os.path.join(DATA_DIR, "encryption.txt")
    file2_path = os.path.join(DATA_DIR, "message.txt")

    plot_space_comparison(file1_path, file2_path)

if __name__ == "__main__":
    main()
