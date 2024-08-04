import re

t = """
{{ 
amut, message, messages, result, resulter, defkatValue, defa, number_two, arit

 }}
"""

splitedCode = re.split(r'\{\{.*?\}\}', t, flags=re.DOTALL)
print(splitedCode)

