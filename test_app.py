from unittest import TestLoader
import unittest

if __name__ == "__main__":
    suite = TestLoader().discover("tests")
    result = None
    # suite.run(result)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print(suite)
