import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from main import add
import pytest 

def test_add():
    assert add(2, 3) == 5
