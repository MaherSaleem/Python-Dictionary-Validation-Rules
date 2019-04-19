import unittest
from ValidationRules.StringRule import StringRule
from ValidationRules.MaxRule import MaxRule
from ValidationRules.MinRule import MinRule
from ValidationRules.EmailRule import EmailRule
from ValidationRules.ArrayRule import ArrayRule
from ValidationRules.InRule import InRule
from ValidationRules.DateRule import DateRule


class TestValidationRules(unittest.TestCase):
    def testStringRuleValidCase(self):
        rule = StringRule('stringAttribute', 'This is a string')
        self.assertEqual(rule.isValid(), True)

    def testStringRuleInValidCase(self):
        rule = StringRule('stringAttribute', 12346)
        self.assertEqual(rule.isValid(), False)

    def testMaxRuleValidCase(self):
        rule = MaxRule('MaxRule', 20, ['25'])
        self.assertEqual(rule.isValid(), True)

    def testMaxRuleInValidCase(self):
        rule = MaxRule('MaxRule', 20, ['15'])
        self.assertEqual(rule.isValid(), False)

    def testMinRuleValidCase(self):
        rule = MinRule('MinRule', 20, ['15'])
        self.assertEqual(rule.isValid(), True)

    def testMinRuleInValidCase(self):
        rule = MinRule('MinRule', 20, ['25'])
        self.assertEqual(rule.isValid(), False)

    def testEmailRuleValidCase(self):
        rule = EmailRule('EmailRule', 'maher@birzeit.edu')
        self.assertEqual(rule.isValid(), True)

    def testEmailRuleInValidCase(self):
        rule = EmailRule('EmailRule', 'maherbirzeit.edu')
        self.assertEqual(rule.isValid(), False)

    def testArrayRuleValidCase(self):
        rule = ArrayRule('ArrayRule', [1, 2, 4, 5])
        self.assertEqual(rule.isValid(), True)

    def testArrayRuleInValidCase(self):
        rule = ArrayRule('ArrayRule', 'string')
        self.assertEqual(rule.isValid(), False)

    def testInRuleValidCase(self):
        rule = InRule('InRule', 'maher', ['ahmad', 'ali', 'sammer', 'maher'])
        self.assertEqual(rule.isValid(), True)

    def testInRuleInValidCase(self):
        rule = InRule('InRule', 'maher', ['ahmad', 'ali', 'sammer'])
        self.assertEqual(rule.isValid(), False)


    def testDateValidCase(self):
        rule = DateRule('DateRule', '13-12-1995')
        self.assertEqual(rule.isValid(), True)

    def testDateInValidCase(self):
        rule = DateRule('DateRule', '40-12-1995')
        self.assertEqual(rule.isValid(), False)

if __name__ == '__main__':
    unittest.main()
