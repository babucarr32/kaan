import sys
import os
import pytest
from src.kaan import kaan

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class TestClass:
    def test_variable_initialization_1(self):
        code = """
            {{messages}}
        """
        result = kaan(code, True)
        assert result == True

    def test_variable_initialization_2(self):
        code = """
            {{
                messages
            }}
        """
        result = kaan(code, True)
        assert result == True
    
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
        result = kaan(code, True)
        assert result == True
    
    def test_variable_initialization_4(self):
        code = """
            {
                messages
            }
        """
        with pytest.raises(SystemExit) as excinfo:
            kaan(code, True)
        assert excinfo.value.code is None
