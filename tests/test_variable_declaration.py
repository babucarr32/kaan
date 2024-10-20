import sys
import os
import pytest
from kaan import kaan

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

    def test_variable_initialization_5(self):
        code = """
            {{messages2344}}
        """
        self.handle_assert(code)

    def test_variable_initialization_6(self):
        code = """
            {{909messages}}
        """
        self.handle_assert(code, systemExit=True)
    
    def test_variable_initialization_7(self):
        code = """
            {{messages2344*******}}
        """
        self.handle_assert(code, systemExit=True)
    
    def test_variable_initialization_8(self):
        code = """
            {{messages2344__}}
        """
        self.handle_assert(code)
    
    def test_variable_initialization_9(self):
        code = """
            {{messages2344****trep}}
        """
        self.handle_assert(code, systemExit=True)
    
    def test_variable_initialization_5(self):
        code = """
            {{messages2344___****}}
        """
        self.handle_assert(code, systemExit=True)
