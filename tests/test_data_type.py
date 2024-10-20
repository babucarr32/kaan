import sys
import os
import pytest
from kaan import kaan

class TestDataType:
    def handle_assert(self, code: str, expect=True, systemExit=False):
        if systemExit:
            with pytest.raises(SystemExit) as excinfo:
                kaan(code, True)
            assert excinfo.value.code is None
        else:
            result = kaan(code, True)
            assert result == expect

    # def test_1(self):
    #     code  = """
    #         ["Mango", "Banana"]
    #     """
    #     self.handle_assert(code)  

    # def test_2(self):
    #     code  = """
    #         "Nanga deff"
    #     """
    #     self.handle_assert(code)  

    # def test_3(self):
    #     code  = """
    #         dega
    #         dudega
    #     """
    #     self.handle_assert(code)        


