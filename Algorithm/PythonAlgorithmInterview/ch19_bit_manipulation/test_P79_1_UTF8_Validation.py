from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch19_bit_manipulation.P79_1_UTF8_Validation import P79_1_UTF8_Validation


class TestP79_1_UTF8_Validation(TestCase):

    def setUp(self):
        self.p79 = P79_1_UTF8_Validation()
    def test_valid_utf8(self):
        data = [197, 130, 1]
        expected = True

        answer = self.p79.validUtf8(data)
        self.assertEqual(expected, answer)
