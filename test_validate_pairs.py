import unittest
import validate_pairs


class TestMyModule(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestMyModule, self).__init__(*args, **kwargs)
        self.short_string_ok = "{[]}"
        self.string_ok = "[()]{}{[()()]()}"
        self.short_string_fail = "{[}]"
        self.string_fail = "[()]}{{[()()]()}"
        self.unknown_string = "[()]{[(*)()]()}"
        self.validate = validate_pairs.ValidatePairs()

    def test_short_string_ok(self):
        self.assertEqual(self.validate.evaluate_string(self.short_string_ok), self.validate.RESULT_OK)

    def test_string_ok(self):
        self.assertEqual(self.validate.evaluate_string(self.string_ok), self.validate.RESULT_OK)

    def test_short_string_fail(self):
        self.assertEqual(self.validate.evaluate_string(self.short_string_fail), self.validate.STRING_ERROR)

    def test_before_string_fail(self):
        self.assertEqual(self.validate.evaluate_string(self.string_fail), self.validate.STRING_ERROR)

    def test_unknown_pair(self):
        self.assertEqual(self.validate.evaluate_string(self.unknown_string), self.validate.UNKNOWN_PAIR)


if __name__ == "__main__":
    unittest.main()
