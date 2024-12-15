import re

comment_pattern = r'%\{.*?%\}'
array_pattern = r'<<(.+?)>>'
const_declaration_pattern = r'def (\w+) := (.+?);'
const_reference_pattern = r'\${(\w+)}'


def check_syntax(input_text):

    const_definitions = re.findall(r'def\s+([a-zA-Z0-9_]+)\s+[^:=]', input_text)
    if const_definitions:
        raise ValueError(
            f"Некорректный синтаксис для объявления константы: {', '.join(const_definitions)}. Используйте := для присваивания.")

    undefined_vars = re.findall(r'\$\{([a-zA-Z0-9_]+)\}', input_text)
    for var in undefined_vars:
        if not re.search(r'def\s+' + var + r'\s+:.+;', input_text):
            raise ValueError(
                f"Использование не определенной константы: {var}. Убедитесь, что константа определена через 'def имя := значение;'")

    return True

def parse_array(array_str):
    elements = array_str.split(',')
    elements = [element.strip() for element in elements]  # Убираем лишние пробелы
    return '[' + ', '.join(elements) + ']'

def parse_const_declaration(declaration):
    match = re.match(const_declaration_pattern, declaration)
    if match:
        name = match.group(1)
        value = match.group(2)
        return f'{name} = {value}'
    return None

def parse_const_reference(reference):
    match = re.match(const_reference_pattern, reference)
    if match:
        return match.group(1)
    return reference

def parse_comments(input_text):
    return re.sub(comment_pattern, '', input_text, flags=re.DOTALL)

def parse_arrays(input_text):
    return re.sub(array_pattern, lambda m: parse_array(m.group(1)), input_text)

def parse_constants(input_text):
    consts = {}
    lines = input_text.splitlines()
    for i, line in enumerate(lines):
        const_declaration = parse_const_declaration(line.strip())
        if const_declaration:
            name, value = const_declaration.split(' = ')
            consts[name] = value
            lines[i] = None

    for i, line in enumerate(lines):
        if line:
            for name, value in consts.items():
                line = re.sub(r'\${' + name + r'}', value, line)
            lines[i] = line

    return '\n'.join(filter(None, lines))

def parse_input(input_text):
    input_text = parse_comments(input_text)
    input_text = parse_arrays(input_text)
    input_text = parse_constants(input_text)

    return input_text
