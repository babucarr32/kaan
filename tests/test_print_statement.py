import sys
import os
import pytest
from src.kaan import kaan

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class TestPrintStatement:
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
            wonel("Hello world")
        """
        self.handle_assert(code)

    def test_2(self):
        code  = """
            wonel("Hello world. " + "Keep coding!!!")
        """
        self.handle_assert(code)

    def test_3(self):
        code  = """
            wonel(f"Hello world")
        """
        self.handle_assert(code, systemExit=True)
    
    def test_4(self):
        code  = """
            wonel('Hello world')
        """
        self.handle_assert(code)
    
    def test_5(self):
        code  = """
            wonel "Hello world"
        """
        self.handle_assert(code, systemExit=True)

    def test_6(self):
        code  = """
            wonel("Hello world");
        """
        self.handle_assert(code, systemExit=True)
    
    def test_7(self):
        code  = """
            wonel("Hello world. \"Keep coding\" ");
        """
        self.handle_assert(code, systemExit=True)
    


