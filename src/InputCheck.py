class InputCheck:
    def __init__(self):
        self._min_value = 1
        self._max_value = 9

    def is_in_range(self, user_input):
        try:
            int(user_input)
        except:
            return False
        return user_input >= self._min_value \
            and user_input <= self._max_value
