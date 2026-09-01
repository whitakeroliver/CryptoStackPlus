# test_cryptostackplus.py
"""
Tests for CryptoStackPlus module.
"""

import unittest
from cryptostackplus import CryptoStackPlus

class TestCryptoStackPlus(unittest.TestCase):
    """Test cases for CryptoStackPlus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoStackPlus()
        self.assertIsInstance(instance, CryptoStackPlus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoStackPlus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
