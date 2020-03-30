import math

from projecteuler.mathlibrary import MathLibrary
from .IEulerSolution import IEulerSolution

class LargestProductSeries(IEulerSolution):
    """
    Solution to problem 8
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    def __init__(self, problem_number = None):
        IEulerSolution.__init__(self)

    def compute(self):
        SIZE_OF_SERIES = 13
        NUMBERS_FROM_SITE = \
            "73167176531330624919225119674426574742355349194934" + \
            "96983520312774506326239578318016984801869478851843" + \
            "85861560789112949495459501737958331952853208805511" + \
            "12540698747158523863050715693290963295227443043557" + \
            "66896648950445244523161731856403098711121722383113" + \
            "30358907296290491560440772390713810515859307960866" + \
            "70172427121883998797908792274921901699720888093776" + \
            "65727333001053367881220235421809751254540594752243" + \
            "52584907711670556013604839586446706324415722155397" + \
            "53697817977846174064955149290862569321978468622482" + \
            "83972241375657056057490261407972968652414535100474" + \
            "82166370484403199890008895243450658541227588666881" + \
            "17866458359124566529476545682848912883142607690042" + \
            "24219022671055626321111109370544217506941658960408" + \
            "07198403850962455444362981230987879927244284909188" + \
            "84580156166097919133875499200524063689912560717606" + \
            "05886116467109405077541002256983155200055935729725" + \
            "71636269561882670428252483600823257530420752963450"

        numbers = list(map(int, NUMBERS_FROM_SITE))
        result = 0

        for position in range(len(numbers) - SIZE_OF_SERIES):
            series = numbers[position : position + SIZE_OF_SERIES]
            trial = MathLibrary.series_product(series)
            if trial > result: result = trial

        return result
