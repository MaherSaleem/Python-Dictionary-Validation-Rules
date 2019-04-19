from DataValidatorParser import DataValidatorParser
from ValidationRules.StringRule import StringRule
from ValidationRules.MaxRule import MaxRule


class DataValidator():

    def __init__(self, data, rules, customAttribute={}, customErrorMessage={}):
        self._data = data
        self._rules = rules
        self._customAttribute = customAttribute
        self._customErrorMessage = customErrorMessage

        self.parsedRules = DataValidatorParser(self).getParsedRules()

    def getErrorMessages(self):
        return list(map(lambda error: error['error_message'], self._validateAllParsedRules()))

    def isValidData(self):
        return all(list(map(lambda error: error['is_valid'], self._validateAllParsedRules())))

    def getFaildAttributes(self):
        return list(set(list(map(lambda error: error['failed_attribute'], self._validateAllParsedRules()))))

    def _validateAllParsedRules(self):
        ret = []
        for parsedRule in self.parsedRules:
            if parsedRule['validationRule'] == 'string':
                validationRule = StringRule(parsedRule['attributeName'], parsedRule['attributeData'],
                                            parsedRule['args'])
            else:
                validationRule = MaxRule(parsedRule['attributeName'], parsedRule['attributeData'], parsedRule['args'])
            if (not validationRule.is_valid()):
                ret.append({
                    'error_message': validationRule.get_validation_default_message(),
                    'is_valid': validationRule.is_valid(),
                    'failed_attribute': parsedRule['attributeName']
                })
        return ret

    '''
           Setters and getters
    '''

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_rules(self):
        return self._rules

    def set_rules(self, rules):
        self._rules = rules

    def get_customAttribute(self):
        return self._customAttribute

    def set_customAttribute(self, customAttribute):
        self._customAttribute = customAttribute

    def get_customErrorMessage(self):
        return self._customErrorMessage

    def set_customErrorMessage(self, customErrorMessage):
        self._customErrorMessage = customErrorMessage
