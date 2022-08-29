import unittest

from creak_sense.predictor import CreakSense


class TestQuery(unittest.TestCase):
    def test_simple_query(self):
        sense = CreakSense("fractalego/creak-sense")
        claim = "Bananas can be found in a grocery list"
        prediction = sense.make_sense(claim)
        self.assertTrue(prediction)

    def test_reason(self):
        sense = CreakSense("fractalego/creak-sense")
        claim = "Bananas can be found in a grocery list"
        predicted = sense.get_reason(claim)
        expected = "Bananas are a staple food"
        self.assertEqual(predicted, expected)
