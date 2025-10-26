# test_cryptosynchronizer.py
"""
Tests for CryptoSynchronizer module.
"""

import unittest
from cryptosynchronizer import CryptoSynchronizer

class TestCryptoSynchronizer(unittest.TestCase):
    """Test cases for CryptoSynchronizer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoSynchronizer()
        self.assertIsInstance(instance, CryptoSynchronizer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoSynchronizer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
