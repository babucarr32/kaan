import re

# t = """
# {{ 
# amut, message, messages, result, resulter, defkatValue, defa, number_two, arit

#  }}
# """

# splitedCode = re.split(r'\{\{.*?\}\}', t, flags=re.DOTALL)
# print(splitedCode)

# code = 'dugal("Lan moneka sa tur? ")'
# r = bool(re.match("dugal(\s+|\s|)(\((\s+|\s|)(\".*\"|\'.*\')(\s+|\s|)\)$)", code))
# print(r)

# c = 'deloh \"Man man      \"'
# t = bool(re.match("deloh(\s+|\s)((\s+|\s|)(\".*\"|\'.*\')$)", c))
# print("REturn: ", t)

# # Validate varible declation

# variable = 'tura = dugal("Lan moneka sa tur? ")'
# isVariable = bool(re.match("[a-zA-Z].+=(\s+|)('|\"|\[|\{|[a-zA-Z0-9]).*(\"|'|\]|\}|[a-zA-Z0-9]|\))$", variable))
# print(isVariable)

# Validate line
# line = "feka bena mohndaw jurom::a"
# lineValid = bool(re.match(r"^[a-zA-Z0-9].*(?<!::)(?<!\}\})$", line))
# print(lineValid)

def validate_line(code: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9].*(?<!(\;|\=|\-|\*|\&|\^|\%|\$|\#|\@|\!|\±|\§|\`|\~|\||\?|\/|\>|\<|\,|\.))(?<!\)\))(?<!::[^)])(?<!}}[^)])(?<!}[^)])(?<!:[^)\s])$", code))

# Test cases
lines = [
    "feka bena mohndaw jurom::",
    "feka bena mohndaw jurom:",
    "feka bena mohndaw jurom)",
    "feka bena mohndaw jurom:;",
    "feka bena mohndaw jurom}:",
    "0000feka bena mohndaw jurom))",
    "feka bena mohndaw jurom}}a",
    "feka bena mohndaw jurom}}",
    "feka bena mohndaw jurom):",  # Should be true
    "valid line example}",
    "valid line example",
    "Bala baba;",
    "deloh \"Man la man la...\"",
    'deloh "Man la man la...";',   # False
    "feka bena mohndaw jurom:;wew",  # Should be false
    'n'
]

for line in lines:
    print(f"'{line}': {validate_line(line)}")