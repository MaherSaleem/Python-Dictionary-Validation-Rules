import unittest
import helpers


class GeneralTest(unittest.TestCase):

    def testGetPythonAttributeByDot(self):
        data = {
            "title": 121,
            "author": {
                "name": "Maher",
                "dob": "11/01/1996",
                "email": "maher@birzeit.edu",
                "friends": ["Chandler", "Monica", "Joey"],
            },
        }
        val = helpers.getDictValue(data, 'author.name')
        self.assertEqual(val, 'Maher')


if __name__ == '__main__':
    unittest.main()
