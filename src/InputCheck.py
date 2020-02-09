class InputCheck:
    def __init__(self):
        self._min_value = 1
        self._max_value = 9

    def is_in_range(self, user_input):
        int_input = 0
        try:
            int_input = int(user_input)
        except:
            return False
        return int_input >= self._min_value \
            and int_input <= self._max_value
