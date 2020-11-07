class ValidatePairs:
    def __init__(self):
        self._pairs = {"{}": 0, "[]": 0, "()": 0}
        self._level = 0
        self.RESULT_OK = 0
        self.UNKNOWN_PAIR = 1
        self.STRING_ERROR = 2

    def evaluate_string(self, string):
        for char in string:
            result = self._evaluate_char(char)
            if result != self.RESULT_OK:
                return result
        if self._level != 0:
            return self.STRING_ERROR
        return self.RESULT_OK

    def _evaluate_char(self, char):
        for item in self._pairs.keys():
            if item[0] == char or item[1] == char:
                if char[0] == item[0]:  # increase level
                    self._level = self._level + 1
                    self._pairs[item] = self._level
                elif self._level == self._pairs[item]:  # decrease level
                    self._level = self._level - 1
                    self._pairs[item] = 0
                    if self._level < 0:  # open before closed
                        return self.STRING_ERROR
                return self.RESULT_OK
        return self.UNKNOWN_PAIR
