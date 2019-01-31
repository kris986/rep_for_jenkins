from app import app
import unittest
import xmlrunner
import time


class BasicTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_pass(self):
        self.assertEqual(10, 7 + 3)

    def test_fail(self):
        self.assertEqual(11, 7 + 3)


if __name__ == '__main__':
    unittest.main(
         testRunner=xmlrunner.XMLTestRunner(output='reports'), failfast=False, buffer=False, catchbreak=False)
