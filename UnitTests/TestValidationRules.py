import unittest
from ValidationRules.StringRule import StringRule
from ValidationRules.MaxRule import MaxRule
from ValidationRules.MinRule import MinRule
from ValidationRules.EmailRule import EmailRule
from ValidationRules.ArrayRule import ArrayRule
from ValidationRules.InRule import InRule
from ValidationRules.DateRule import DateRule
from ValidationRules.NumberRule import NumberRule
from ValidationRules.PhoneRule import PhoneRule
from ValidationRules.RequiredRule import RequiredRule


class TestValidationRules(unittest.TestCase):
    def testStringRuleValidCase(self):
        rule = StringRule('stringAttribute', 'This is a string')
        self.assertEqual(rule.is_valid(), True)

    def testStringRuleInValidCase(self):
        rule = StringRule('stringAttribute', 12346)
        self.assertEqual(rule.is_valid(), False)

    def testMaxRuleValidCase(self):
        rule = MaxRule('MaxRule', 20, ['25'])
        self.assertEqual(rule.is_valid(), True)

    def testMaxRuleInValidCase(self):
        rule = MaxRule('MaxRule', 20, ['15'])
        self.assertEqual(rule.is_valid(), False)

    def testMinRuleValidCase(self):
        rule = MinRule('MinRule', 20, ['15'])
        self.assertEqual(rule.is_valid(), True)

    def testMinRuleInValidCase(self):
        rule = MinRule('MinRule', 20, ['25'])
        self.assertEqual(rule.is_valid(), False)

    def testEmailRuleValidCase(self):
        rule = EmailRule('EmailRule', 'maher@birzeit.edu')
        self.assertEqual(rule.is_valid(), True)

    def testEmailRuleInValidCase(self):
        rule = EmailRule('EmailRule', 'maherbirzeit.edu')
        self.assertEqual(rule.is_valid(), False)

    def testArrayRuleValidCase(self):
        rule = ArrayRule('ArrayRule', [1, 2, 4, 5])
        self.assertEqual(rule.is_valid(), True)

    def testArrayRuleInValidCase(self):
        rule = ArrayRule('ArrayRule', 'string')
        self.assertEqual(rule.is_valid(), False)

    def testInRuleValidCase(self):
        rule = InRule('InRule', 'maher', ['ahmad', 'ali', 'sammer', 'maher'])
        self.assertEqual(rule.is_valid(), True)

    def testInRuleInValidCase(self):
        rule = InRule('InRule', 'maher', ['ahmad', 'ali', 'sammer'])
        self.assertEqual(rule.is_valid(), False)

    def testDateValidCase(self):
        rule = DateRule('DateRule', '13-12-1995')
        self.assertEqual(rule.is_valid(), True)

    def testDateInValidCase(self):
        rule = DateRule('DateRule', '40-12-1995')
        self.assertEqual(rule.is_valid(), False)

    def testNumberValidCase(self):
        rule = NumberRule('NumberRule', 6)
        self.assertEqual(rule.is_valid(), True)

    def testNumberInValidCase(self):
        rule = NumberRule('NumberRule', 'maher')
        self.assertEqual(rule.is_valid(), False)

    def testPhoneValidCase(self):
        rule = PhoneRule('NumberRule', '+970599123456')
        self.assertEqual(rule.is_valid(), True)

    def testPhoneInValidCase(self):
        rule = PhoneRule('NumberRule', '+asdasdas')
        self.assertEqual(rule.is_valid(), False)

    def testRequiredInValidCase1_None(self):
        rule = RequiredRule('RequiredRule', None)
        self.assertEqual(rule.is_valid(), False)

    def testRequiredInValidCase2_EmptyString(self):
        rule = RequiredRule('RequiredRule', '')
        self.assertEqual(rule.is_valid(), False)

    def testRequiredValidCase(self):
        rule = RequiredRule('RequiredRule', 'Maher')
        self.assertEqual(rule.is_valid(), True)


if __name__ == '__main__':
    unittest.main()
