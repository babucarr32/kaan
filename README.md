# Kaan
A wolof programming language, it is aim to make introduction to programming easy for
complete wolof speaking beginners in programming. I believe writing code in your native/traditional will make one better understand what a program does, and make one easily understand how to write the basics of a programming language.

Kaan is built un top of (python)[https://www.python.org]. At the end, kaan is compiled to compiled to python code, and executed. Meaning at the end, are running python.

Kaan is by no way meant to be a high level programming, that should/can be used for building real life/production ready applications. The language is kept simple and minimal intentionally, to serve as a helper to introduction to programming.  

## What is programming?
Programming is the technique of giving a computer a set of instruction to execute.
These instruction can be in the form of text or binary (zeros and ones).

## Tutorial
### Variable
A variable is a container used to store data. To use or assign a value to a variable, you have to first declare it within `{{...}}`
Example.
```
{{sumaTur}}

sumaTur = "Baboucarr"
```

You can also assign a variable to a variable. Multiple variable names should be separated with a coma `,`

```
{{
    sumaTur,
    saTur
}}

sumaTur = "Baboucarr"
saTur = sumaTur
```

### Data types
The following are the available data types in kaan.

1. string
2. list
3. boolean

### string
The string data type is represented with either single or  double quote. In other words,
anything with single or double quote is represented as a string.
Example.
```
"Nuyu naalen"
'Nuyu naalen'
```

### List
The list data type is represented with `[]`. Lists are use for storing a collection of data.
You can think of it as a container where you store things.
Example.
```
lekayii = ["Mango", "Banana", "Mboha"]
```

### Boolean
The boolean data type is represented with `dega` or `dudegah`. `dega` means true, and `dudegah`
means false.
Example.
```
sunekeh dega:
    wonel("Degalah")
```

### Operators
There are two types of operators in kaan. `Arithemtic` and `Comparison` operators.

`Arithmetic operators` are use for arithmetic operations. They are expressed in within square braces `{...}`. Current available operators are `yoka`, `wanyi`, `sedoh`, and `ful`

`yoka` equals `+`
`wanyi` equals `-`
`ful` equals `*`
`sedoh` equals `/`

Using an unknown operator throws an error.

Usage Example
```
{{
    saAt,
    senAt,
    sumaAt,
    sunyuAt
}}

saAt = {fuk yoka nyaar}
wonel("saAt " + saAt)

senAt = {fuk ful nyaar}
wonel("senAt " + senAt)

sumaAt = {fuk wanyi nyaar}
wonel("sumaAt " + sumaAt)

sunyuAt = {fuk sedoh nyaar}
wonel("sunyuAt " + sunyuAt)
```

`Comparison operators` are used for checking the equality of two values or more values. Available operators are `mohemak` and `emutak`.

`mohemak` is used for checking the equality of two values`==`
`emutak` is used for checking the unequality of two values`!=`

Example
```
{{
    tur,
    saTur,
    sumaTur,
}}

satur = "Ali"
sumaTur = "baboucarr"
tur = {satur mohemak sumaTur}
wonel(tur)
```

### Conditions


### Function
A function is a named block of code, that is called over and over again. In kaan, functions 
are denoted by `defal`. And are called by invoking the function by name, with parenthesis `defal()`
Example
```
defal nuyu():
    wonel("Nanga def")
nuyu()
```
The function also accepts arguments. All arguments must be declared at the top level first.
Example
```
{{ at }}

defal magWollaHaleh(at):
    sunekeh at mohopah fuk:
        wonel("Yow mag nga")
    kon:
        wonel("Yow haleh nga")
magWollaHaleh(fuk)
```

Functions can also be assigned to variables.
Example
```
{{ at, sumaMag }}

defal magWollaHaleh(at):
    sunekeh at mohopah fuk:
        wonel("Yow mag nga")
    kon:
        wonel("Yow haleh nga")

sumaMag = magWollaHaleh
sumaMag(fuk)

```


### Looping
There are two looping techniques in kaan, `puru` and `feka`.

`puru` is used for looping over a list of items.
`feka` is used for looping over a condition that holds true.

Example for `puru`
```
{{
    leka,
    lekayii,
}}

lekayii = ["Mango", "Banana", "Mboha"]

puru leka bunekasi lekayii:
    wonel("Lekabi moi " + leka)
```

Example for `feka`
```
{{ satur }}

faka satur emutak "Baboucarr":
    satur = dugal("Lan mohneka satur? ")
    wonel("Satur bi moi " + satur)
```

## Contribution Guideline
Create a virtual env `python3 -m venv path/to/venv` and install python
Run with python3 -m pytest