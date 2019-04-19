import unittest
from ValidationRules.StringRule import StringRule
from ValidationRules.MaxRule import MaxRule
from ValidationRules.MinRule import MinRule
from ValidationRules.EmailRule import EmailRule


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
        rule = MinRule('MaxRule', 20, ['15'])
        self.assertEqual(rule.isValid(), True)

    def testMinRuleInValidCase(self):
        rule = MinRule('MaxRule', 20, ['25'])
        self.assertEqual(rule.isValid(), False)

    def testEmailRuleValidCase(self):
        rule = EmailRule('EmailRule', 'maher@birzeit.edu')
        self.assertEqual(rule.isValid(), True)

    def testEmailRuleInValidCase(self):
        rule = EmailRule('EmailRule', 'maherbirzeit.edu')
        self.assertEqual(rule.isValid(), False)


if __name__ == '__main__':
    unittest.main()
