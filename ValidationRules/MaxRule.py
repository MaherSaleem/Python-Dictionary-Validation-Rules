from ValidationRule import ValidationRule


class MaxRule(ValidationRule):
    def __init__(self, attribute_name, attribute_data, args=[]):
        super().__init__(attribute_name, attribute_data, args)
        self._args = list(map(int, self._args))

    def is_valid(self):
        return self.get_attribute_data() <= self.maxValue

    def get_validation_default_message(self):
        return "The %s field must at max %s" % (self.get_attribute_name(), self.maxValue)

    @property
    def maxValue(self):
        return self.get_args()[0]
