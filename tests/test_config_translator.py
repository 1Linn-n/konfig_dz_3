import unittest
from config_translator.parser import parse_input, check_syntax
from config_translator.translator import convert_to_toml

class TestConfigTranslator(unittest.TestCase):

    def test_check_syntax_valid(self):
        valid_config = """
        def my_const := 10;
        [example]
        value1 = ${my_const}
        """
        try:
            check_syntax(valid_config)
        except Exception as e:
            self.fail(f"check_syntax raised {type(e).__name__} unexpectedly!")

    def test_check_syntax_invalid(self):
        invalid_config = """
        def my_const 10;  # Ошибка: нет :=
        [example]
        value1 = ${my_const}
        """
        with self.assertRaises(ValueError):
            check_syntax(invalid_config)

    def test_convert_to_toml(self):
        config = """
        def my_const := 10;

        [example]
        value1 = ${my_const}
        value2 = <<1, 2, 3>>
        """
        expected_toml = """
        my_const = 10

        [example]
        value1 = my_const
        value2 = [1, 2, 3]
        """
        result = convert_to_toml(config)
        self.assertEqual(result.strip(), expected_toml.strip())

if __name__ == '__main__':
    unittest.main()
