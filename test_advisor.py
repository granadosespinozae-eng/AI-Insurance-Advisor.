import unittest
from insurance_advisor import recommend


class RecommendationTests(unittest.TestCase):
    def test_life(self):
        self.assertEqual(recommend({"dependents": True})[0], ["Life insurance"])

    def test_health(self):
        self.assertEqual(recommend({"health": True})[0], ["Health insurance"])

    def test_tie(self):
        self.assertEqual(recommend({"dependents": True, "retirement": True})[0],
                         ["Life insurance", "Retirement plan"])

    def test_no_priority(self):
        self.assertEqual(recommend({})[0], [])


if __name__ == "__main__":
    unittest.main()
