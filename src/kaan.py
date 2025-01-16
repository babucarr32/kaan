import re
import os
import subprocess
from tokens import lex_tokens
from tokens import numbers

arithmetics_values = {}

def is_function(code: str) -> bool:
    return bool(re.search('[a-zA-Z]+\(.*\)$', code))

def is_variable_name_declared(name: str, variables: [str]) -> bool:
    return name in variables

def get_function_name(function_name: str) -> str:
    func_name = function_name.replace(" ", '').split("(")[0]
    return func_name

def is_creating_function(code: str) ->  bool:
    return bool(re.search('^defal [a-zA-Z]+\(.*\)', code))

def is_invoking_function(code: str) ->  bool:
    return bool(re.findall(r'^[a-zA-Z]+\(([a-zA-Z].*|\s+|)\)$', code))

def is_function_arguments_valid(code: str, variables: list[str]):
    argsString = re.findall(r'\([a-zA-Z0-9].*\)$', code)
    if len(argsString):
        args = argsString[0][1:-1].replace(" ", '').split(",")
        for arg in args:
            if is_token_in_lex_tokens(arg) or arg not in variables or arg in numbers.keys():
                return {'is_valid': False, 'value': arg}
    return {'is_valid': True, 'value': ''}

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
    if bool(re.match('^wonel\(', code)):
        return True
    # (?<!::) is a negative lookbehind assertion.
    return bool(re.match(r"^[a-zA-Z0-9].*(?<!(\;|\=|\-|\*|\&|\^|\%|\$|\#|\@|\!|\±|\§|\`|\~|\||\?|\/|\>|\<|\,|\.))(?<!\)\))(?<!::[^)])(?<!}}[^)])(?<!}[^)])(?<!:[^)\s])$", code))

def is_for_loop(code: str) -> bool:
    return bool(re.match(r"^puru", code))

def leading_whitespace_length(s):
    trimmed_string = s.lstrip()
    return len(s) - len(trimmed_string)

def tab_next_line(code: str) -> bool:
    return bool(re.match('[a-z].*:$', code))

def split_code(code: str):
    clean_code = code.strip()
    if is_creating_function(clean_code):
        return re.split(':|\t', clean_code)

    if clean_code.startswith("wonel("):
        return [clean_code]

    if is_invoking_function(clean_code):
        return [clean_code]
    
    return re.split(' |:|\t', clean_code)

def is_token_in_lex_tokens(key: str) -> bool:
    return key in lex_tokens or key in numbers

def is_print_statement(text: str) -> bool:
    return bool(re.search('^wonel\(', text))

def validate_initialized_variable(variable_name: str) -> bool:
    is_valid = bool(re.search(r'^[A-Za-z]+([0-9a-zA-Z]|_)+$', variable_name)) and not " " in variable_name
    
    if not is_valid: 
        print(f"""
Tur letter keseh la wara kumaaseh wola letter ak number wola letter ak _ {variable_name}
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

def value_error(variable_name: str):
    print(f"""
Tur bii amut, {variable_name}.
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
    splittedCode = re.split('\{\{.*?\}\}', code, flags=re.DOTALL)
    if len(splittedCode) > 1:
        return splittedCode[1]
    return splittedCode[0]

def is_doing_arithmetic_operation(code: str) -> bool:
    return bool(re.match("^{(\s|[a-zA-Z]).*(\s|[a-zA-Z])}\B", code))

def validate_value(variable_value: str, variables:[str], variable_name = '') -> bool:
    is_referencing_value = re.match("[a-zA-Z0-9]", variable_value)
    is_func_declared = False
    is_func = is_function(variable_value)
    
    if is_func:
        func_name = get_function_name(variable_value)
        is_func_declared = is_variable_name_declared(func_name, variables)
        return is_func_declared

    is_input = is_taking_input(variable_value)
    if variable_name:
        if is_referencing_value and not is_func and not is_input or not is_func_declared:
            if variable_value in variables or variable_value in numbers.keys():
                if variable_name not in numbers.keys():
                    numbers[variable_name] = variable_value
                return True
            return False
    
    if is_doing_arithmetic_operation(variable_value):
        values = re.split("({|\s|})", variable_value)
        for i in values:
            if not re.match("(\{|\})", i.strip()):
                if i.strip():
                    if not i in lex_tokens and not i in numbers:
                        return False
    return True

def validate_print_statement(code: str, variables: [str]) -> bool:
    is_printing_string = bool(re.match(r'(wonel\(".*"\)|wonel\(\'.*\'\))$', code))
    is_valid = True
    bad_content = ''
    
    if not is_printing_string:
        # print_content = re.findall('\([a-zA-Z].+\)$', code)[0][1:-1]
        print_content = re.findall('\(.*\)$', code)[0][1:-1]
        if print_content in lex_tokens or validate_value(print_content, variables):
            pass
        else:
            bad_content = print_content
            is_valid = False

    if is_valid:
        return is_valid
    else:
        print(f"""
Khejna danga juum {bad_content} warut neka fofu
                  {"-"*len(bad_content)} \nwola\n""")
        variable_declaration_error(bad_content, )
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
                    if type(numbers[i]) == int:
                        calc += f"{numbers[i]} "
                    else: 
                        num_value = numbers[i]
                        calc += f"{numbers[num_value]} "
                else:
                    variable_declaration_error(i)
                    quit()
    
    result = ''
    evaluated = eval(calc)
    last_number = max(list(numbers.values()))
    if evaluated <= last_number:
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
    else:
        value_error(code)
        quit()
    if result:
        arithmetics_values[code] = result
                
def validate_tokens(code: str, declared_variables: [str]) -> str:
    is_valid = True
    previous_value = ""
    should_tab_next_line = False
    previous_value_tab_length = 0
    line_codes = split_by_new_line(code)

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

                is_variable_valid = validate_value(variable_value, declared_variables, variable_name)
                
                is_arithmetic = is_doing_arithmetic_operation(variable_value)
                if is_arithmetic:
                    handle_arithmetic(variable_value)

                else:
                    if not is_variable_valid:
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
                    is_using_for_loop = is_for_loop(strippedLine)
                    for token in tokens:
                        if token:
                            if is_print_statement(token):
                                validate_print_statement(token, declared_variables)
                            else:
                                if not is_function(token):
                                    # make sure token is not ''
                                    is_valid = is_token_in_lex_tokens(token) or token in declared_variables or is_string(token)
                                    if not is_valid:
                                        if is_using_for_loop:
                                            variable_declaration_error(token, declared_variables)
                                            quit()
                                        else:
                                            print("breaking...", token)
                                            break
                                else:
                                    func = token.split('defal ')[-1].strip()
                                    func_name = get_function_name(func)
                                    is_func_declared = is_variable_name_declared(func_name, declared_variables)
                                    if is_func_declared:
                                        result = is_function_arguments_valid(func, declared_variables)
                                        print("Validating:...", result)
                                        is_valid = result["is_valid"]
                                        invalid_value = result["value"]

                                        if not is_valid:
                                            variable_declaration_error(invalid_value, declared_variables)
                                            quit()
                                    else:
                                        variable_declaration_error(func_name, declared_variables)
                                        quit()
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
     # Regex pattern to match keys not inside quotes
    pattern_template = r'(?<!["\'])\b{}\b(?!["\'])(?=(?:[^"\']*(?:["\'][^"\']*["\']))*[^"\']*$)'

            
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
            pattern = pattern_template.format(re.escape(key))  # Escape the key to safely use in the regex
            new_code = re.sub(pattern, str(lex_tokens[key]), new_code)

    return new_code

def kaan(__code__ = '', __dev__ = False, filePath = ''):
    if __code__:
        variables = get_variables(__code__)
        if len(variables):
            if not is_initialized_variables_valid(variables):
                quit()
        
        new_code = get_code(__code__)
        is_code_valid = validate_tokens(new_code, variables)
    else:
        # read the code
        with open(filePath) as f:
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
        outputPath = f"{os.getcwd()}/build.py"
        with open(outputPath, "w") as f:
            f.write(compiled_code)
        f.close()
        
        # run the built file
        subprocess.run(["python3", outputPath])

    if __dev__:
        return is_code_valid
