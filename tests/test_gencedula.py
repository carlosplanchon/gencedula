#!/usr/bin/env python3

import re
import unittest

from gencedula import (
    calculate_digito_verificador,
    format_cedula,
    generate_cedula,
    verify_cedula,
)


class TestCalculateDigitoVerificador(unittest.TestCase):
    def test_known_example(self):
        # 1.234.567-2
        self.assertEqual(calculate_digito_verificador(1_234_567), 2)

    def test_zero_padded_cedula(self):
        # 0.000.000-0
        self.assertEqual(calculate_digito_verificador(0), 0)

    def test_out_of_range(self):
        for cedula in (-1, 10_000_000):
            with self.subTest(cedula=cedula):
                with self.assertRaises(ValueError):
                    calculate_digito_verificador(cedula)


class TestVerifyCedula(unittest.TestCase):
    def test_valid_cedulas(self):
        for cedula in (12_345_672, 46_308_006, 41_064_007):
            with self.subTest(cedula=cedula):
                self.assertTrue(verify_cedula(cedula))

    def test_invalid_cedulas(self):
        for cedula in (12_345_671, 46_308_007, -1, 100_000_000):
            with self.subTest(cedula=cedula):
                self.assertFalse(verify_cedula(cedula))


class TestFormatCedula(unittest.TestCase):
    def test_seven_digit_number(self):
        self.assertEqual(format_cedula(12_345_672), "1.234.567-2")
        self.assertEqual(format_cedula(46_308_006), "4.630.800-6")

    def test_shorter_numbers(self):
        self.assertEqual(format_cedula(9_876_543), "987.654-3")
        self.assertEqual(format_cedula(1_236), "123-6")
        self.assertEqual(format_cedula(0), "0-0")

    def test_out_of_range(self):
        for cedula in (-1, 100_000_000):
            with self.subTest(cedula=cedula):
                with self.assertRaises(ValueError):
                    format_cedula(cedula)

    def test_formats_generated_cedulas(self):
        pattern = re.compile(r"^\d{1,3}(?:\.\d{3})*-\d$")
        for _ in range(100):
            self.assertRegex(format_cedula(generate_cedula()), pattern)


class TestGenerateCedula(unittest.TestCase):
    def test_generated_cedulas_are_valid(self):
        for _ in range(1000):
            self.assertTrue(verify_cedula(generate_cedula()))

    def test_range_and_step(self):
        for _ in range(100):
            cedula = generate_cedula(
                start=4_000_000, stop=5_000_000, step=200
            )
            numero = cedula // 10
            self.assertTrue(4_000_000 <= numero < 5_000_000)
            self.assertEqual((numero - 4_000_000) % 200, 0)

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            generate_cedula(start=-1)
        with self.assertRaises(ValueError):
            generate_cedula(stop=10_000_001)


if __name__ == "__main__":
    unittest.main()
