import sys
import os
import pytest
from src.kaan import kaan

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class TestForLoop:
    def handle_assert(self, code: str, expect=True, systemExit=False):
        if systemExit:
            with pytest.raises(SystemExit) as excinfo:
                kaan(code, True)
            assert excinfo.value.code is None
        else:
            result = kaan(code, True)
            assert result == expect

    def test_1(self):
        code  = """
            fruits = ["Mango", "Banana"]
            puru fruit bunekasi fruits:
                wonel(fruit)
        """
        self.handle_assert(code, systemExit=True)  

    def test_2(self):
        code  = """
            {{ fruits }}
            fruits = ["Mango", "Banana"]
            puru fruit bunekasi fruits:
                wonel(fruit)
        """
        self.handle_assert(code, systemExit=True)  

    def test_3(self):
        code  = """
            {{ fruits, fruit }}
            fruits = ["Mango", "Banana"]
            puru fruit bunekasi fruits:
                wonel(fruit)
        """
        self.handle_assert(code)        


