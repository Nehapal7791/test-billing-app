"""Tests for tax module."""

from src.tax import calculate_tax, get_tax_rate


def test_standard_rate():
    assert get_tax_rate("standard") == 0.20


def test_calculate_tax_standard():
    assert calculate_tax(100.0) == 20.0


def test_calculate_tax_reduced():
    assert calculate_tax(100.0, "reduced") == 5.0
