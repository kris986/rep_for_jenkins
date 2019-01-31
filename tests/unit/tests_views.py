from app import app
from app import create_app
import unittest


class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_pass(self):
        self.assertEqual(10, 7 + 3)

    def test_fail(self):
        self.assertEqual(10,7 + 3)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reports'))
