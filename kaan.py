import re
import subprocess

lex_tokens = {
    "sunekeh": "if",
    "mohopah": ">",
    "mohndaw": "<",
    "wonel": "print",
    ":": ":",
    "kon": "else",
    "puru": "for",
    "bunekasi": "in",
    "feka": "while",
    "defal": "def",
    "dama": "break",
    "mohemak": "==",
    "dugal": "input",
    "yoka": "+",
    "deloh": "return",
    "waanyi": "-",
    "sedoh": "/",
    "ful": "*",
}

numbers = {
    "neen": 0,
    "bena": 1,
    "nyaar": 2,
    "nyet": 3,
    "nyenent": 4,
    "jurom": 5,
    "juromBen": 6,
    "juromNyaar": 7,
    "juromNyet": 8,
    "juromNyenent": 9,
    "fuk": 10,
}

arithmetics_values = {}

def is_function(code: str):
    return bool(re.search('[a-zA-Z]+\(\)$', code))

# def get_code_content(code: str):
#     splitted_content = code.split("}}")
#     print("SPlitted", len(splitted_content), code)
#     content = "".join(splitted_content)
#     return content


def split_by_new_line(code: str) -> bool:
    return re.split('\n', code)

def is_returning(code: str) -> bool:
    return bool(re.match('deloh ', code))

def validate_return(code: str) -> bool:
    return bool(re.match("deloh(\s+|\s)((\s+|\s|)(\".*\"|\'.*\')$)", code))

def is_taking_input(code: str) -> bool:
    return  bool(re.match("dugal(\s+|\s|)(\((\s+|\s|)(\".*\"|\'.*\')(\s+|\s|)\)$)", code))

def is_string(code: str) -> bool:
    return bool(re.match('(\"|\')[a-zA-Z0-0]+(\"|\')', code))

def validate_line(code: str) -> bool:
    # (?<!::) is a negative lookbehind assertion.
    return bool(re.match(r"^[a-zA-Z0-9].*(?<!(\;|\=|\-|\*|\&|\^|\%|\$|\#|\@|\!|\±|\§|\`|\~|\||\?|\/|\>|\<|\,|\.))(?<!\)\))(?<!::[^)])(?<!}}[^)])(?<!}[^)])(?<!:[^)\s])$", code))

def leading_whitespace_length(s):
    trimmed_string = s.lstrip()
    return len(s) - len(trimmed_string)

def tab_next_line(code: str) -> bool:
    return bool(re.match('[a-z].*:$', code))

def split_code(code: str):
    clean_code = code.strip()
    if clean_code.startswith("wonel("):
        return [clean_code]
    
    return re.split(' |:|\t', clean_code)

def is_token_in_lex_tokens(key: str) -> bool:
    return key in lex_tokens or key in numbers

def is_print_statement(text: str) -> bool:
    return bool(re.search('^wonel\(', text))

def validate_initialized_variable(variable_name: str) -> bool:
    is_valid = bool(re.match('[A-Za-z]', variable_name)) and not " " in variable_name
    
    if not is_valid: 
        print(f"""
Tur letter keseh la wara kumaaseh {variable_name}
                                  {"-" * len(variable_name)}
""")
    return is_valid

def variable_declaration_error(variable_name: str, variables = []):
    if len(variables):
        print(f"""
Khejna danga juum, {variable_name} nekut si turii.
                   {"-" * len(variable_name)}
{variables}
""")
    else:
        print(f"""
Khejna danga juum, {variable_name} nekut si turii.
                   {"-" * len(variable_name)}
""")
        
def indentation_error(variable_name: str, showDifferentMsg = False):
    if showDifferentMsg:
        print(f"""
Khejna danga juum, {variable_name} dafa wara def dara.
                   {"-" * len(variable_name)}
""")
    else:
        print(f"""
Khejna danga juum, {variable_name} nyenent palace la wara am si boraam.
                   {"-" * len(variable_name)}
""")

def get_variables(code: str):
    variable_names = []
    variable_scope = re.findall('\{\{.*?\}\}', code, flags=re.DOTALL)
    if len(variable_scope):
        sanitize_variables = re.sub("(\n|\t)", "", variable_scope[0])
        split_variables = re.split("(\{\{|\}\}|,)", sanitize_variables)
        
        for i in split_variables:
            ii = i.strip()
            if ii and ii != "}}" and ii != "{{" and ii != ",":
                variable_names.append(ii)
    return variable_names


def is_initialized_variables_valid(variable_names: [str]) -> bool:
    is_valid = True
    for v in variable_names:
        if not validate_initialized_variable(v):
            is_valid = False
            break
    return is_valid

def get_code(code: str) -> str:
    splitedCode = re.split('\{\{.*?\}\}', code, flags=re.DOTALL)
    if len(splitedCode) > 1:
        return splitedCode[1]
    return splitedCode[0]

def is_doing_arithmetic_operation(code: str) -> bool:
    return bool(re.match("^{(\s|[a-zA-Z]).*(\s|[a-zA-Z])}\B", code))

def validate_value(variable_value: str, variables:[str]) -> bool:
    is_referencing_value = re.match("[a-zA-Z0-9]", variable_value)
    is_func = is_function(variable_value)
    is_input = is_taking_input(variable_value)
    if is_referencing_value and not is_func and not is_input:
        return variable_value in variables or variable_value in numbers.keys()
    
    if is_doing_arithmetic_operation(variable_value):
        values = re.split("({|\s|})", variable_value)
        for i in values:
            if not re.match("(\{|\})", i.strip()):
                if i.strip():
                    if not i in lex_tokens and not i in numbers:
                        return False
    return True

def validate_print_statement(code: str, text: str, variables: [str]) -> bool:
    is_printing_string = bool(re.search('^wonel\(\'.+\'\)\B|^wonel\(\".+\"\)\B', text))
    is_valid = True
    bad_content = ''
    
    if not is_printing_string:
        print_content = re.split('^wonel\(|\)', text)
        for content in print_content:
            # make sure token is not ''
            if content:
                if content in lex_tokens or validate_value(content, variables):
                    pass
                else:
                    bad_content = content
                    is_valid = False
                    break

    if is_valid:
        return is_valid
    else:
        print(f"""
Khejna danga juum {bad_content} warut neka fofu
                  {"-"*len(bad_content)}""")
        quit()

def is_declaring_variable(code: str) -> bool:
    return  bool(re.match("[a-zA-Z].+=(\s+|)('|\"|\[|\{|[a-zA-Z0-9]).*(\"|'|\]|\}|[a-zA-Z0-9])\B", code))

def get_remainder(n: int) -> int:
    return n % 1

def is_whole_number(n: int) -> bool:
    return not bool(get_remainder(n))

def get_number_key_by_value(value: int) -> str:
    for i in numbers:
        if int(value) == numbers[i]:
            return i

def handle_arithmetic(code: str) -> None:
    values = re.split("({|\s|})", code)
    calc = ''
    for i in values:
        if not re.match("(\{|\})", i.strip()):
            if i.strip():
                if i in lex_tokens:
                    calc += f"{lex_tokens[i]} "
                elif i in numbers:
                    calc += f"{numbers[i]} "
                else:
                    variable_declaration_error(i)
                    quit()
    
    result = ''
    evaluated = eval(calc)
    for i in numbers:
        if evaluated > 0:
            remainder = get_remainder(evaluated)
            if remainder:
                [first_num, last_num] = str(round(remainder, 1)).split(".")
                result = f"{get_number_key_by_value(first_num)} tomb {get_number_key_by_value(last_num)}"
                break
            else:
                if evaluated == numbers[i]:
                    result = i
                    break
        else:
            if is_whole_number(evaluated):
                absolute_number = abs(evaluated)
                if absolute_number == numbers[i]:
                    result = f"-{i}"
                    break
    if result:
        arithmetics_values[code] = result
                
def validate_tokens(code: str, declared_variables: [str]) -> str:
    line_codes = split_by_new_line(code)
    is_valid = True
    should_tab_next_line = False
    previous_value = ""
    previous_value_tab_length = 0


    for line in line_codes:
        strippedLine = line.strip()
        if validate_line(strippedLine) or should_tab_next_line:
            # validate indentations
            if should_tab_next_line:
                white_space_len = leading_whitespace_length(line)

                if previous_value_tab_length:
                    if white_space_len != previous_value_tab_length + 4:
                        indentation_error(strippedLine)
                        quit()

                if white_space_len % 4 > 0 or not white_space_len:
                    if not strippedLine:
                        indentation_error(previous_value, True)
                    else:
                        indentation_error(strippedLine)
                    quit()
            should_tab_next_line = tab_next_line(strippedLine)
            previous_value_tab_length = leading_whitespace_length(line)

            if should_tab_next_line:
                previous_value = strippedLine

            if is_declaring_variable(strippedLine):
                variable_name = line.split("=")[0].strip()
                if not variable_name in declared_variables:
                    variable_declaration_error(variable_name, declared_variables)
                    quit()
                    
                variable_value = re.split("[a-zA-Z].+=", line)[1].strip()

                is_variable_valid = validate_value(variable_value, declared_variables)
                
                is_arithmetic = is_doing_arithmetic_operation(variable_value)
                
                if is_arithmetic:
                    handle_arithmetic(variable_value)

                if not is_variable_valid:
                    print("*****", is_variable_valid)
                    variable_declaration_error(variable_value, declared_variables)
                    quit()

            elif is_taking_input(strippedLine):
                pass

            elif is_returning(strippedLine):
                is_return_valid = validate_return(strippedLine)
                if not is_return_valid:
                    print(f"""
    Khejna danga juum {strippedLine} warut neka fofu
                    {"-"*len(strippedLine)}""")
                    quit()
                
            else:
                if is_valid:
                    tokens = split_code(line)
                    for token in tokens:
                        if token:
                            if is_print_statement(token):
                                validate_print_statement(code, token, declared_variables)
                            else:
                                if not is_function(token):
                                    # make sure token is not ''
                                    is_valid = is_token_in_lex_tokens(token) or token in declared_variables or is_string(token)
                                    if not is_valid:
                                        print("breaking...", token)
                                        break
                else:
                    break
        else:
            if strippedLine:
                print(f"""
Khejna danga juum {strippedLine} warut neka fofu
                  {"-"*len(strippedLine)}""")
                quit()
    return is_valid

def compile_to_python(code: str, declared_variables:[str]) -> str:
    new_code = ""
            
    if len(declared_variables):
        for v in declared_variables:
            new_code += f"{v}=''\n"
    
    new_code += f"\n\n"
    
    for v in numbers:
        new_code +=f"{v}={numbers[v]}\n"

    new_code += code
    if len(arithmetics_values.keys()):
        for key in arithmetics_values:
            new_code = new_code.replace(key, f"\"{str(arithmetics_values[key])}\"")
            
    for key in lex_tokens.keys():
        if key not in arithmetics_values.values() and key not in numbers.keys():
            new_code = new_code.replace(key, str(lex_tokens[key]))
    
    return new_code

def __main__():
    # read the code
    with open("./test.vy") as f:
        code  = f.read()
        variables = get_variables(code)
        if len(variables):
            if not is_initialized_variables_valid(variables):
                quit()
        
        new_code = get_code(code)
        is_code_valid = validate_tokens(new_code, variables)
    f.close()
    
    if is_code_valid:
        compiled_code = compile_to_python(new_code, variables)

        # write the compiled code to build.py
        with open("./build.py", "w") as f:
            f.write(compiled_code)
        f.close()
        
        # run the built file
        subprocess.run(["python3", "build.py"])

if __name__ == "__main__":
    __main__()

# print(token[":"])

"""
for x in items:
    print(x)

num = 0
while num < 10:
    print(num)
    num += 1

TODO
1. Fix casting str and number
2. Fix print issue
3. (check for variables within code block)
4. Make sure variable name on contains letter or letter with number or _only
sunekeh nyet mohopah nyaar:
        wonel("'True\"'")
kon:
        wonel(Falseisdifesfdf)
5. Numbers should be separated from lex tokens to prevent tokens like kon from passing value checks
6. Keyboard interupt error on taking input. (Potential fix use string template to wrap input with try catch and display custom error)
7. Test wonel(name())
8. defkatValue = tur(): (Enhance the error message for this line )

NOTE:
variable must be initialized
variable name with newline in between is treated as single variable
{{
 amut
tur
}}
becomes "amuttur"

variable declaration should happen in only one scope.
{{amuttur}}

not
{{amuttur}}
{{amuttur}}

The code below will be ignored during compilation.
But, python will throw an error during execution.
sunekeh bena mohopah nyaar:
        wonel("Dega")
        amut = "1012"
kon:
        wonel(amut)

Allowed data types [] {} number and string
Only positive numbers as allowed()
floats are rounded to to the nearest number .75 becomes .8
{bena yoka nyaar}asds
    Throws error. Fix print statement

first line after code block cannot be whitespace
    sunekeh bena:

        bena
    (This will throw error)

    (Correct)
    sunekeh bena:
        bena
"""
