import sys
import os
import pytest
from src.kaan import kaan

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class TestFunctions:
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
            defal tur():
                wonel("Babucarr")
        """
        self.handle_assert(code)

    def test_2(self):
        code  = """
            defal tur(bena, nyaar, feka):
                wonel("Babucarr")
        """
        self.handle_assert(code, systemExit=True)
    
    def test_3(self):
        code  = """
            defal tur(santa):
                wonel("Babucarr")
        """
        self.handle_assert(code, systemExit=True)
    
    def test_4(self):
        code  = """
            {{santa, at}}
            defal tur(santa, at):
                wonel("Babucarr")
        """
        self.handle_assert(code)

    def test_5(self):
        code  = """
            {{santa, at}}
            defal tur(santa, at, nyet):
                wonel("Babucarr")
        """
        self.handle_assert(code)
    
    def test_6(self):
        code  = """
            {{santa, at}}
            defal tur (santa, at):
                wonel("Babucarr")
        """
        self.handle_assert(code, systemExit=True)
  

