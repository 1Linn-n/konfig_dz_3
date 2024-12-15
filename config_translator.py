import argparse
from config_translator.parser import parse_input, check_syntax  # Импортируем check_syntax
from config_translator.translator import convert_to_toml


def main():
    # Создание парсера командной строки
    parser = argparse.ArgumentParser(description="Конвертер конфигурации в TOML")
    parser.add_argument('input_file', help="Путь к входному конфигурационному файлу")
    args = parser.parse_args()

    # Открытие файла и чтение конфигурации
    with open(args.input_file, 'r', encoding='utf-8') as file:  # Обеспечим чтение с кодировкой UTF-8
        input_text = file.read()

    try:
        # Проверка синтаксиса
        check_syntax(input_text)  # Проверяем на ошибки синтаксиса

        # Обработка текста
        processed_text = parse_input(input_text)
        toml_output = convert_to_toml(processed_text)

        # Вывод в формате TOML
        print(toml_output)
    except Exception as e:
        # Вывод ошибки на русском
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()
