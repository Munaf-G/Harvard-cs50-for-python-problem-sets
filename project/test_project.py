import unittest

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

class TestUnitConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)

    def test_kilometers_to_miles(self):
        self.assertAlmostEqual(kilometers_to_miles(1), 0.621371)
        self.assertAlmostEqual(kilometers_to_miles(10), 6.21371)
        self.assertAlmostEqual(kilometers_to_miles(0), 0)

    def test_miles_to_kilometers(self):
        self.assertAlmostEqual(miles_to_kilometers(1), 1.609344, places=6)
        self.assertAlmostEqual(miles_to_kilometers(10), 16.09344, places=5)
        self.assertAlmostEqual(miles_to_kilometers(0), 0)

    def test_pounds_to_kilograms(self):
        self.assertAlmostEqual(pounds_to_kilograms(1), 0.453592)
        self.assertAlmostEqual(pounds_to_kilograms(10), 4.53592)
        self.assertAlmostEqual(pounds_to_kilograms(0), 0)

    def test_kilograms_to_pounds(self):
        self.assertAlmostEqual(kilograms_to_pounds(1), 2.20462, places=5)
        self.assertAlmostEqual(kilograms_to_pounds(10), 22.0462, places=4)
        self.assertAlmostEqual(kilograms_to_pounds(0), 0)

if __name__ == "__main__":
    unittest.main()
