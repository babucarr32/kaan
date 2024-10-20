import sys
import os
import pytest
from kaan import kaan

class TestIndentation:
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
            sunekeh bena mohopah nyaar:
                wonel("True")
            kon:
                wonel("False")
        """
        self.handle_assert(code)

    def test_2(self):
        code  = """
            sunekeh bena mohopah nyaar:
                wonel("True")
            kon:
                 wonel("False")
        """
        self.handle_assert(code, systemExit=True)
    
    def test_3(self):
        code  = """
            sunekeh bena mohopah nyaar:
                wonel("True")
            kon:
            wonel("False")
        """
        self.handle_assert(code, systemExit=True)

    def test_4(self):
        code  = """
            sunekeh bena mohopah nyaar:
                wonel("True")
            kon: wonel("False")
        """
        self.handle_assert(code, systemExit=True)

    def test_5(self):
        code  = """
        {{result}}
            result = {bena ful nyaar}
        """
        self.handle_assert(code, systemExit=True)
    
    def test_6(self):
        code  = """
            {{result}}
            result = {bena ful nyaar}
        """
        self.handle_assert(code, systemExit=True)
    
    def test_7(self):
        code  = """
            {{result}}
        result = {bena ful nyaar}
        """
        self.handle_assert(code)


