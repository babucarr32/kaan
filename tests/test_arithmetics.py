import sys
import os
import pytest
from src.kaan import kaan

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class TestArithmetics:
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
            {bena ful nyaar}
        """
        self.handle_assert(code)

    def test_2(self):
        code  = """
            {{result}}
            result = {bena ful nyaar}
        """
        self.handle_assert(code)
    
    def test_3(self):
        code  = """
            results = {bena ful nyaar}
        """
        self.handle_assert(code, systemExit=True)
    
    def test_4(self):
        code  = """
            {{result}}
            result = {bena ful nyaar}}
        """
        self.handle_assert(code, systemExit=True)

    def test_5(self):
        code  = """
            {{result, result2}}
            result = {bena ful nyaar}
            result2=result
        """
        self.handle_assert(code)
    
    def test_6(self):
        code  = """
            {{result, result2}}
            result = {bena ful nyaar}
            results=result
        """
        self.handle_assert(code, systemExit=True)
    
    def test_7(self):
        code  = """
            {{result, result2}}
            result = {bena ful nyaar yoka bena}
            result2=result
        """
        self.handle_assert(code)

    def test_8(self):
        code  = """
            {{result, result2}}
            result = {bena ful nyaar}
            result2=result
        """
        self.handle_assert(code)
         
    def test_9(self):
        code = """
            {{ current }}

            current = fuk
            current = {current waanyi bena}  
            wonel(current)
                      
        """
        self.handle_assert(code)

