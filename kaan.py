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
    "ligey": "def",
    "mohemak": "==",
    "dugal": "input",
    "bena": 1,
    "nyaar": 2,
    "nyet": 3,
    "nyenent": 4,
    "fuk": 5
}

numbers = {
    "bena": 1,
    "nyaar": 2,
    "nyet": 3,
    "nyenent": 4,
    "fuk": 5
}

def split_by_new_line(code: str):
    return re.split('\n', code)

def split_code(code: str):
    clean_code = code.strip()
    if clean_code.startswith("wonel("):
        return [clean_code]
    
    return re.split(' |:|\t', clean_code)

def is_token_in_lex_tokens(key: str) -> bool:
    return key in lex_tokens

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

def variable_declaration_error(variable_name: str, variables: [str]):
    print(f"""
Khejna danga juum, {variable_name} nekut si turii.
                   {"-" * len(variable_name)}
{variables}
""")

def validate_line(text: str) -> bool:
    print("Received ", text)
    return bool(re.search('[a-zA-Z].+(\)|:|\s+|"|[0-9])\B', text))

def get_variables(code: str):
    variable_names = []
    variable_scope = re.findall('\{\{.*?\}\}', code, re.DOTALL)
    if len(variable_scope):
        sanitize_variables = re.sub("(\n|\t)", "", variable_scope[0])
        split_variables = re.split("({{|}}|,)", sanitize_variables)
        
        for i in split_variables:
            ii = i.strip()
            if ii and ii != "}}" and ii != "{{" and ii != ",":
                variable_names.append(ii)
    return variable_names


def is_initialized_variables_valid(variable_names: [str]) -> bool:
    is_valid = True
    for v in variable_names:
        if (not validate_initialized_variable(v)):
            is_valid = False
            break
    return is_valid

def get_code(code: str) -> str:
    splitedCode = re.split('\{\{.*?\}\}', code, re.DOTALL)
    if len(splitedCode) > 1:
        return splitedCode[1]
    return splitedCode[0]

def validate_value(variable_value: str, variables:[str]) -> bool:
    is_referencing_value = re.match("[a-zA-Z0-9]", variable_value)
    if is_referencing_value:
        return variable_value in variables or variable_value in numbers.keys()
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

def is_declaring_variable(code: str):
    return  bool(re.match("[a-zA-Z].+=(\s+|)('|\"|\[|\{|[a-zA-Z0-9]).*(\"|'|\]|\}|[a-zA-Z0-9])\B", code))

def validate_tokens(code: str, variables: [str]) -> str:
    line_codes = split_by_new_line(code)
    is_valid = True
    for line in line_codes:
#         is_line_valid = validate_line(line)
#         print("is_line_valid", is_line_valid)
        if is_declaring_variable(line):
            variable_name = line.split("=")[0].strip()
            
            if not variable_name in variables:
                variable_declaration_error(variable_name, variables)
                quit()
                
            variable_value = re.split("[a-zA-Z].+=", line)[1].strip()

            is_variable_valid = validate_value(variable_value, variables)

            if not is_variable_valid:
                variable_declaration_error(variable_value, variables)
                quit()
        else:
            if is_valid:
                tokens = split_code(line)
                for token in tokens:
                    if token:
                        if is_print_statement(token):
                            validate_print_statement(code, token, variables)
                        else:
                            # make sure token is not ''
                            is_valid = is_token_in_lex_tokens(token)
                            if not is_valid:
                                break
            else:
                break
    return is_valid

def compile_to_python(code: str, declared_variables:[str]) -> str:
    new_code = ""
    
    if len(declared_variables):
        for v in declared_variables:
            new_code += f"{v}=''\n"
    
    new_code += code
    for key in lex_tokens.keys():
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


"""