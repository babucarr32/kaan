import re
import subprocess

lex_token = {
    "sunekeh": "if",
    "mohopah": ">",
    "wonel": "print",
    ":": ":",
    "kon": "else"
}
def tokenizer(value:str):
    tokens = re.split(' |\n|\t', value)
    generated = ""
    firstLoop = True
#     print(tokens)
    
    for t in tokens:
        if t:
            if t == ":":
                generated += ":\n    "
            else:
                if "wonel" in t:
                    printStatement = re.split('\(|\)', t)
                    _print_ = printStatement[0]
                    printValue = printStatement[1]
                    generated += f"{lex_token[_print_]}({printValue})"
                elif t in lex_token.keys():
                    if firstLoop:
                        generated += f"{lex_token[t]}"
                    else:
                        if lex_token[t] == "else":
                            generated += f"\n{lex_token[t]}"
                        else:
                            generated += f" {lex_token[t]}"
                else:
                    if firstLoop:
                        generated += f"{t}"
                    else:
                        generated += f" {t}"
        firstLoop = False
    return generated

def __main__():
    with open("./test.vy") as f:
        content  = f.read()
        code = tokenizer(content)
    f.close()    
    
    with open("./build.py", "w") as f:
        f.write(code)
    f.close()
    
    subprocess.run(["python", "build.py"])
    
__main__()
# print(token[":"])

"""
if 1 > 2:
    print(True)
"""