# test_postgresqltutorial.py
"""
Tests for PostgresqlTutorial module.
"""

import unittest
from postgresqltutorial import PostgresqlTutorial

class TestPostgresqlTutorial(unittest.TestCase):
    """Test cases for PostgresqlTutorial class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PostgresqlTutorial()
        self.assertIsInstance(instance, PostgresqlTutorial)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PostgresqlTutorial()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
