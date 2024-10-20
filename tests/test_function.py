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
            {{santa, at, tur}}
            defal tur(santa, at):
                wonel("Babucarr")
        """
        self.handle_assert(code)

    def test_5(self):
        code  = """
            {{santa, at, tur}}
            defal tur(santa, at, nyet):
                wonel("Babucarr")
        """
        self.handle_assert(code)
    
    def test_6(self):
        code  = """
            {{santa, at, tur}}
            defal tur (santa, at):
                wonel("Babucarr")
        """
        self.handle_assert(code, systemExit=True)

    def test_7(self):
        code  = """
            {{santa, at, tur}}
            defal tur (santa, at):
                wonel("Babucarr")
            tur()
        """
        self.handle_assert(code, systemExit=True)

    def test_8(self):
        code  = """
            {{santa, at, tur}}
            defal tur (santa, at):
                wonel("Babucarr")
            tur("Babu")
        """
        self.handle_assert(code, systemExit=True)
    
    def test_8(self):
        code  = """
            {{santa, at, tur}}
            defal tur (santa, at):
                wonel("Babucarr")
            tur("Babu", 'Jurom')
        """
        self.handle_assert(code)

    def test_9(self):
        code  = """
            {{santa, at, tur}}
            defal tur (santa, at):
                wonel("Babucarr")
            tur("babu", 40)
        """
        self.handle_assert(code, systemExit=True)
    
    def test_10(self):
        code  = """
            {{santa, at, sumaTur, sumaAt, tur}}
            defal tur (santa, at):
                wonel("Babucarr")
            tur(sumaTur, sumaAt)
        """
        self.handle_assert(code)
    
    def test_11(self):
        code  = """
            {{
                at,
                tur,
                santa,
                sumaAt,
                sumaTur,
            }}

            sumaTur="Babucarr"
            sumaAt=Jurom

            defal tur (santa, at):
                wonel("Babucarr")
            tur(sumaTur, sumaAt)
        """
        self.handle_assert(code)

    def test_12(self):
        code  = """
            {{
                at,
                tur,
                santa,
                sumaAt,
                sumaTur,
                jelalTur
            }}

            sumaTur="Babucarr"
            sumaAt=Jurom

            defal tur (santa, at):
                wonel("Babucarr")
            jelalTur = tur
            jelalTur(sumaTur, sumaAt)
        """
        self.handle_assert(code)
    
    def test_13(self):
        code  = """
            {{ at }}
            defal tur ():
                wonel("Babucarr")
            tur()
        """
        self.handle_assert(code, systemExit=True)
    
    def test_14(self):
        code  = """
            {{ at }}
            defal tur ():
                wonel("Babucarr")
            wonel(tur())
        """
        self.handle_assert(code, systemExit=True)
    
    def test_15(self):
        code  = """
            {{ maam }}
            defal maam(at):
                wonel("Yow maam nga")
            maam()
        """
        self.handle_assert(code, systemExit=True)

    def test_16(self):
        code  = """
            defal magWollaHaleh(at):
                wonel("Yow mag nga" + 20)
        """
        self.handle_assert(code)
  

