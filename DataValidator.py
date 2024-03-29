from DataValidatorParser import DataValidatorParser
from config import config
from helpers import *

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
        rulesClasses = self.get_rules_classes()
        for parsedRule in self.parsedRules:
            validationRuleClass = get_classs(rulesClasses[parsedRule['validationRule']])
            validationRule = validationRuleClass(parsedRule['attributeName'], parsedRule['attributeData'],
                                                 parsedRule['args'], parsedRule['errorMessage'])
            if (not validationRule.is_valid()):
                ret.append({
                    'error_message': validationRule.get_error_message(),
                    'is_valid': validationRule.is_valid(),
                    'failed_attribute': parsedRule['attributeName']
                })
        return ret

    def get_rules_classes(self):
        rules = config['supported_rules']
        packageName = 'ValidationRules'
        classesMapping = {}
        for rule in rules:
            className = rule.capitalize() + 'Rule'
            classesMapping[rule] = packageName + '.' + className + '.' + className
        return classesMapping

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
