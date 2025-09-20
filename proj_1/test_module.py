import unittest
import mean_var_std as calculator

class TestMeanVarStd(unittest.TestCase):

    def compare(self, result, expected):
        if isinstance(result, list) and isinstance(expected, list):
            for i in range(len(result)):
                self.compare(result[i], expected[i])
        else:
            self.assertAlmostEqual(result, expected, places=6)

    def test_calculate(self):
        result = calculator.calculate([0,1,2,3,4,5,6,7,8])
        expected = {
            'mean': [[3.0, 4.0, 5.0],
                     [1.0, 4.0, 7.0],
                     4.0],
            'variance': [[6.0, 6.0, 6.0],
                         [0.6666666667, 0.6666666667, 0.6666666667],
                         6.6666666667],
            'standard deviation': [[2.449489743, 2.449489743, 2.449489743],
                                   [0.8164965809, 0.8164965809, 0.8164965809],
                                   2.581988897],
            'max': [[6, 7, 8],
                    [2, 5, 8],
                    8],
            'min': [[0, 1, 2],
                    [0, 3, 6],
                    0],
            'sum': [[9, 12, 15],
                    [3, 12, 21],
                    36]
        }

        for key in expected:
            self.compare(result[key], expected[key])

if __name__ == "__main__":
    unittest.main()
