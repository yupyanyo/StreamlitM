# test_streamlitml.py
"""
Tests for StreamlitML module.
"""

import unittest
from streamlitml import StreamlitML

class TestStreamlitML(unittest.TestCase):
    """Test cases for StreamlitML class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StreamlitML()
        self.assertIsInstance(instance, StreamlitML)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StreamlitML()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
