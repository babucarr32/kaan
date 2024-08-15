import sys
import os
import pytest
from src.kaan import kaan

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class TestVariableAssignment:
    def handle_assert(self, code: str, expect=True, systemExit=False):
        if systemExit:
            with pytest.raises(SystemExit) as excinfo:
                kaan(code, True)
            assert excinfo.value.code is None
        else:
            result = kaan(code, True)
            assert result == expect
    
    def test_1(self):
        code = """ username="user101" """
        self.handle_assert(code, systemExit=True)
    
    def test_2(self):
        code = """
            {{username}}
            username="user101"
        """
        self.handle_assert(code)
    
    def test_3(self):
        code = """
            {{username}}
            USERNAME="user101"
        """
        self.handle_assert(code, systemExit=True)

    def test_4(self):
        code = """
            {{username}}
            username      =        "user101"
        """
        self.handle_assert(code)

    def test_5(self):
        code = """
            {{username}}
            username
                ="user101"
        """
        self.handle_assert(code, systemExit=True)

    def test_6(self):
        code = """
            {{username, password}}
            username="user101"
            password=2345
        """
        self.handle_assert(code, systemExit=True)

    def test_7(self):
        code = """
            {{username, password}}
            username="user101"
            password=username
        """
        self.handle_assert(code)

    def test_8(self):
        code = """
            {{fruits}}
            fruits=["Mango", "Banana"]
        """
        self.handle_assert(code)
    
    def test_9(self):
        code = """
            {{fruits}}
            fruits=["Mango", "Banana"];
        """
        self.handle_assert(code, systemExit=True)
    
    def test_10(self):
        code = """
            {{fruits}}
            fruits=[]
        """
        self.handle_assert(code)
    
    def test_11(self):
        code = """
            {{fruits}}
            fruits=       []
        """
        self.handle_assert(code)
    
    def test_12(self):
        code = """
            {{fruits}}
            fruits=["Mango", "Banana"]]
        """
        self.handle_assert(code, systemExit=True)