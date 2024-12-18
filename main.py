main
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def encode_message(message, cover_text):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_index = 0
    words = cover_text.split()
    encoded_text = []

    try:
        max_bits = len(words) - 1
        if len(binary_message) > max_bits:
            logging.error(f"Ошибка: Сообщение слишком длинное для текста-контейнера. Доступно {max_bits} бит, требуется {len(binary_message)}.")
            return None

        for i, word in enumerate(words):
            encoded_text.append(word)
            if i < len(words) - 1 and binary_index < len(binary_message):
                bit = binary_message[binary_index]
                encoded_text.append("  " if bit == '1' else " ") # Два пробела для 1, один для 0
                binary_index += 1

        return " ".join(encoded_text)

    except Exception as e:
        logging.exception(f"Произошла ошибка во время кодирования: {e}")
        return None

def main():
    DATA_DIR = "D:\\study\\STEGO3"  # Замените на вашу директорию
    message_file_path = os.path.join(DATA_DIR, "message.txt")
    output_file_path = os.path.join(DATA_DIR, "encryption.txt")

    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(message_file_path, "r", encoding="utf-8") as f:
            cover_text = f.read().strip() # Убираем лишние пробелы в начале и конце
        hidden_message = input("Введите сообщение для скрытия: ")
        stego_text = encode_message(hidden_message, cover_text)
        if stego_text:
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(stego_text)
            print(f"Закодированное сообщение сохранено в {output_file_path}")
        else:
            print("Ошибка кодирования.")
    except FileNotFoundError as e:
        print(f"Файл {message_file_path} не найден: {e}")
    except OSError as e:
        print(f"Ошибка системы: {e}")
    except Exception as e:
        logging.exception(f"Произошла неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()