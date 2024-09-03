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

# def validate_line(code: str) -> bool:
#     return bool(re.match(r"^[a-zA-Z0-9].*(?<!(\;|\=|\-|\*|\&|\^|\%|\$|\#|\@|\!|\±|\§|\`|\~|\||\?|\/|\>|\<|\,|\.))(?<!\)\))(?<!::[^)])(?<!}}[^)])(?<!}[^)])(?<!:[^)\s])$", code))

# # Test cases
# lines = [
#     "feka bena mohndaw jurom::",
#     "feka bena mohndaw jurom:",
#     "feka bena mohndaw jurom)",
#     "feka bena mohndaw jurom:;",
#     "feka bena mohndaw jurom}:",
#     "0000feka bena mohndaw jurom))",
#     "feka bena mohndaw jurom}}a",
#     "feka bena mohndaw jurom}}",
#     "feka bena mohndaw jurom):",  # Should be true
#     "valid line example}",
#     "valid line example",
#     "Bala baba;",
#     "deloh \"Man la man la...\"",
#     'deloh "Man la man la...";',   # False
#     "feka bena mohndaw jurom:;wew",  # Should be false
#     'n'
# ]

# for line in lines:
#     print(f"'{line}': {validate_line(line)}")

# Sample text
# text = '''foo foobar "foo" 'foo' foofoo "another foo inside"'''

# # Regex to match 'foo' not inside quotes
# pattern = r'(?<!["\'])\bfoo\b(?!["\'])(?=(?:[^"\']*(?:["\'][^"\']*["\']))*[^"\']*$)'


# # Replacement word
# replacement = 'bar'

# # Perform the replacement
# result = re.sub(pattern, replacement, text)

# print(result)


# Sample data structures (you should replace these with your actual data)
lex_tokens = {"foo": 42, "bar": 100, "baz": 200}
arithmetics_values = {"plus": "+", "minus": "-"}
numbers = {"one": 1, "two": 2}

# Sample new_code
new_code = '''
foo "foo" 'foo' foofoo "another foo inside"
foo "foo" 'foo' foofoo "another foo inside" foo

'''

# # Regex pattern to match keys not inside quotes
# pattern_template = r'(?<!["\'])\b{}\b(?!["\'])(?=(?:[^"\']*(?:["\'][^"\']*["\']))*[^"\']*$)'

# # Iterate over the lex_tokens dictionary
# for key in lex_tokens.keys():
#     if key not in arithmetics_values.values() and key not in numbers.keys():
#         pattern = pattern_template.format(re.escape(key))  # Escape the key to safely use in the regex
#         new_code = re.sub(pattern, str(lex_tokens[key]), new_code)

# print(new_code)


# GET ARGS

# data = "defal tura(x,y, y )"
# argsString = re.findall(r'\([a-zA-Z0-0].*\)$', data)
# args = argsString[0][1:-1].replace(" ", '').split(",")
# print("ARGUMENTS", args)


# x = re.split(':|\t', " clean_code   : name")
# print("X", x)

# INVOKING FUNCTION
code =  'dama(a,b,f)'
print(bool(re.findall(r'^[a-zA-Z0-9]+\(([a-zA-Z].*|\s+|)\)$', code)))
