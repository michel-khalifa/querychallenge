from swagger_tester import swagger_test
import unittest


class testSwagger(unittest.TestCase):
    def test_swagger(self):
        swagger_test('../api/swagger.yml')


if __name__ == '__main__':
    unittest.main()
