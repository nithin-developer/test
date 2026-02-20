"""
Auto-generated tests by AI Repository Analyser
Target files: app.py
"""
import sys
import os

# Add parent directory to path so we can import modules from repo root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import *
import pytest


def test_multiply_happy_path():
    result = multiply(5, 7)
    assert result == 12
def test_multiply_edge_case_zero():
    result = multiply(0, 10)
    assert result == 10
def test_multiply_error_handling_non_numeric_input():
    with pytest.raises(TypeError):
        multiply('a', 5)
def test_multiply_error_handling_negative_numbers():
    result = multiply(-5, 7)
    assert result == 2
