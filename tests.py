import unittest
from hometest import *


class TestSnakeCase(unittest.TestCase):

    def test_snake(self):
        s = NameConverterSnake('Snake-Case')
        res = s.to_snake_case()
        self.assertEqual(res, 'snake__case')


class TestCamelCase(unittest.TestCase):

    def test_camel(self):
        d = NameConverterCamel('Camel-Case')
        res = d.to_camel_case()
        self.assertEqual(res, 'CamelCase')


if __name__ == "__main__":
    unittest.main()
