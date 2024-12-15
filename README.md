# Config Translator
# Конфиг Транслятор

## 1. Общее описание

Этот проект представляет собой инструмент командной строки для преобразования конфигурационных файлов с пользовательским синтаксисом в формат TOML. Входной текст в формате конфигурации анализируется, проверяется на синтаксические ошибки, и после этого преобразуется в формат TOML, который может быть использован в различных приложениях.

Проект поддерживает:
- Многострочные комментарии.
- Массивы в виде `<< ... >>`.
- Объявления и использование констант.
- Преобразование переменных в выражениях `${}`.
  
### Основные возможности:
- Преобразование конфигураций в формат TOML.
- Проверка синтаксиса конфигурационного файла.
- Поддержка вычислений на этапе трансляции (через константы).

## 2. Описание всех функций и настроек

### Функции:

1. **`check_syntax(input_text)`**  
   Проверяет синтаксис конфигурационного файла на наличие ошибок.
   - Аргумент: `input_text` (строка) — текст конфигурационного файла.
   - Возвращает: `True`, если ошибок не обнаружено.
   - Вызывает исключение `ValueError`, если в конфигурации обнаружены синтаксические ошибки.

2. **`convert_to_toml(config_text)`**  
   Преобразует конфигурационный текст в формат TOML.
   - Аргумент: `config_text` (строка) — текст конфигурации.
   - Возвращает: преобразованный текст в формате TOML.

3. **`parse_input(file_path)`**  
   Читает конфигурационный файл, указанного пути, и передает его на обработку.
   - Аргумент: `file_path` (строка) — путь к конфигурационному файлу.
   - Возвращает: строку с конфигурацией, которая была прочитана из файла.

## 3. Описание команд для сборки проекта

Для использования этого инструмента, выполните несколько шагов:

### Установка зависимостей:

Для работы проекта требуется Python 3.7+.

1. Перейдите в каталог проекта:

```sh
cd config_translator_project
```

2. Установите зависимости:

```sh
pip install -r requirements.txt
```

### Запуск проекта:

Чтобы использовать инструмент, запустите команду в терминале:

```sh
python config_translator.py <path_to_config.conf>
```

Где `<path_to_config.conf>` — это путь к вашему входному конфигурационному файлу.

### Пример:

```sh
python config_translator.py config.conf
```

Эта команда прочитает конфигурацию из файла `config.conf`, проверит синтаксис, преобразует его в формат TOML и выведет результат в консоль.

## 4. Примеры использования

Пример конфигурационного файла:

```sh
def my_const := 10;

%{ 
Это многострочный 
комментарий 
%}

[example] 
value1 = ${my_const} 
value2 = <<1, 2, 3>>
```

Результат:

```toml
my_const = 10

[example]
value1 = 10
value2 = [1, 2, 3]
```

## 5. Результаты прогона тестов
Для проверки корректности работы инструмента, были написаны тесты с использованием библиотеки unittest.

Чтобы запустить тесты, используйте следующую команду:

```sh
python -m unittest discover tests
```

Пример результатов прогона тестов:

```sh
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```