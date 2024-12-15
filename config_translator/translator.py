import re

def convert_to_toml(config_text):

    config_text = re.sub(r'%\{.*?%\}', '', config_text, flags=re.DOTALL)

    config_text = re.sub(r'<<([^>]+)>>', r'[\1]', config_text)

    config_text = re.sub(r'\$\{([a-zA-Z0-9_]+)\}', r'\1', config_text)

    config_text = re.sub(r'def\s+([a-zA-Z0-9_]+)\s*:=\s*(.*?);', r'\1 = \2', config_text)

    return config_text