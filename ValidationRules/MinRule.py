from ValidationRule import ValidationRule


class MinRule(ValidationRule):
    def __init__(self, *args):
        super().__init__(*args)
        self._args = list(map(int, self._args))

    def is_valid(self):
        return self.get_attribute_data() >= self.minValue

    def get_validation_default_message(self):
        return "The %s field must at least %s" % (self.get_attribute_name(), self.minValue)

    @property
    def minValue(self):
        return self.get_args()[0]
