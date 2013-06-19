__author__ = 'sasaki'


def main():
    print("main")
    pass


class Intervals():
    def __init__(self, N):
        self.N = N
        self.cycle = int(N * (N + 1) / 2)
        self.series = [x for x in range(1, N + 1)]
        self.series.extend(range(1, N))
        self.counter = [0] * self.cycle

    def countUp(self, i):
        self.counter[i - 1] += 1

    def sum(self, beginning, width):
        assert beginning >= 1
        assert width >= 1
        if beginning + width - 1 > len(self.series):
            raise IndexError
        s = sum(self.series[beginning - 1:beginning - 1 + width])
        return s

    def countUpForWidth(self, width):
        for i in (range(1, self.N + 1)):
            s = self.sum(i, width)
            self.countUp(s)

    def getCounter(self, i):
        if i < 1: raise IndexError
        return self.counter[i - 1]

    def getCycle(self):
        return self.cycle


import unittest


class _TestCase(unittest.TestCase):
    def setUp(self):
        self.N = 3
        self.intervals = Intervals(self.N)

    def testInit(self):
        self.assertIsInstance(self.intervals, Intervals)
        self.assertIsInstance(self.intervals.series, list)
        self.assertEqual(len(self.intervals.series), self.N * 2 - 1)
        self.assertEqual(self.intervals.cycle * 2, self.intervals.N * (self.intervals.N + 1))

    def testSum(self):
        self.assertEqual(self.intervals.series, [1, 2, 3, 1, 2])
        self.assertEqual(self.intervals.sum(1, 1), 1)
        self.assertEqual(self.intervals.sum(2, 1), 2)
        self.assertEqual(self.intervals.sum(3, 1), 3)
        self.assertEqual(self.intervals.sum(1, 2), 3)
        self.assertEqual(self.intervals.sum(2, 2), 5)
        self.assertEqual(self.intervals.sum(3, 2), 4)
        self.assertEqual(self.intervals.sum(1, 3), 6)
        self.assertEqual(self.intervals.sum(2, 3), 6)
        self.assertEqual(self.intervals.sum(3, 3), 6)
        self.assertRaises(IndexError, lambda: self.intervals.sum(4, 6))

    def testCountUp(self):
        self.assertEqual(self.intervals.counter[0], 0)
        self.intervals.countUp(1)
        self.assertEqual(self.intervals.counter[0], 1)
        self.intervals.countUp(1)
        self.assertEqual(2, self.intervals.getCounter(1))
        self.assertRaises(IndexError, lambda: self.intervals.getCounter(0))
        self.assertEqual(self.N * 2 - 1, self.intervals.getLength())
        self.assertEqual(0, self.intervals.getCounter(self.intervals.N))
        self.assertRaises(IndexError, lambda: self.intervals.getCounter(self.intervals.N + 1))

    def testCountUpForWidth1(self):
        self.assertEqual(self.intervals.series, [1, 2, 3, 1, 2])
        self.assertEqual(self.intervals.counter, [0, 0, 0])
        self.intervals.countUpForWidth(1)
        self.assertEqual(self.intervals.counter, [1, 1, 1, 0, 0])

    def testCountUpForWidth2(self):
        self.assertEqual(self.intervals.series, [1, 2, 3, 1, 2])
        self.assertEqual(self.intervals.counter, [0, 0, 0, 0, 0])
        self.intervals.countUpForWidth(2)
        self.assertEqual(self.intervals.counter, [0, 0, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
    main()