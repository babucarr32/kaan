import re
import subprocess

lex_token = {
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
    "dugal": "input"
}

def generate_code(data: str) -> str:
    new_data = data
    for key in lex_token.keys():
        new_data = new_data.replace(key, lex_token[key])
    return new_data

def __main__():
    with open("./test.vy") as f:
        content  = f.read()
        code = generate_code(content)
    f.close()    
    
    with open("./build.py", "w") as f:
        f.write(code)
    f.close()
    
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
"""