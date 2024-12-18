import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def decode_message(stego_text):
    binary_message = ""
    decoded_message = ""

    try:
        logging.info(f"Обрабатываемый текст: {stego_text}")
        i = 0
        while i < len(stego_text):
            if stego_text[i] == ' ':
                count = 0
                while i < len(stego_text) and stego_text[i] == ' ':
                    count += 1
                    i += 1
                if count == 3:  # Два пробела - это '0'
                    binary_message += "0"
                elif count == 4:  # Три пробела - это '1'
                    binary_message += "1"
            else:
                i += 1

        if len(binary_message) % 8 != 0:
            logging.warning(f"Длина бинарного сообщения не кратна 8 ({len(binary_message)}). Обрезаем неполный байт.")
            binary_message = binary_message[:len(binary_message) - (len(binary_message) % 8)]

        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i + 8]
            if len(byte) == 8:
                try:
                    decoded_message += chr(int(byte, 2))
                except ValueError as e:
                    logging.error(f"Ошибка преобразования байта '{byte}': {e}")
            else:
                logging.warning(f"Неполный байт (должно быть 8 бит): {byte}. Пропускаем.")

        logging.info(f"Раскодированный двоичный код: {binary_message}")
        return decoded_message
    except Exception as e:
        logging.exception(f"Произошла ошибка во время декодирования: {e}")
        return None
def main():
    DATA_DIR = "D:\\study\\STEGO3"  # Замените на вашу директорию
    encryption_file_path = os.path.join(DATA_DIR, "encryption.txt")
    decode_file_path = os.path.join(DATA_DIR, "decoded_message.txt")

    try:
        with open(encryption_file_path, "r", encoding="utf-8") as f:
            stego_text = f.read()
        decoded_message = decode_message(stego_text)
        if decoded_message:
            with open(decode_file_path, "w", encoding="utf-8") as outfile:
                outfile.write(decoded_message)
            print(f"Расшифрованное сообщение сохранено в {decode_file_path}")
            print(f"Расшифрованное сообщение: {decoded_message}")
        else:
            print("Ошибка расшифровки.")
    except FileNotFoundError as e:
        print(f"Файл {encryption_file_path} не найден: {e}")
    except OSError as e:
        print(f"Ошибка системы: {e}")
    except Exception as e:
        logging.exception(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()