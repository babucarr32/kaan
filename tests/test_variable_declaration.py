import sys
import os
import pytest
from src.kaan import kaan

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class TestVariableDeclaration:
    def handle_assert(self, code: str, expect=True, systemExit=False):
        if systemExit:
            with pytest.raises(SystemExit) as excinfo:
                kaan(code, True)
            assert excinfo.value.code is None
        else:
            result = kaan(code, True)
            assert result == expect

    def test_variable_initialization_1(self):
        code = """
            {{messages}}
        """
        self.handle_assert(code)


    def test_variable_initialization_2(self):
        code = """
            {{
                messages
            }}
        """
        self.handle_assert(code)
    
    def test_variable_initialization_3(self):
        code = """
            {{
                amut,

                
                                                defa,
arit,       
                tura,
                                result,
                message,messages,
                resulter, number_two,
                defkatValue,     }} 
        """
        self.handle_assert(code)

    
    def test_variable_initialization_4(self):
        code = """
            {
                messages
            }
        """
        self.handle_assert(code, systemExit=True)
