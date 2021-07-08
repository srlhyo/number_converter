#This program is a number converter. Transforms numbers into binary and hexadecimal.

def dec_bin():
    _usr_input = int(input("\nDecimal: "))
    _usr_output = lambda _usr_input: format(_usr_input, 'b')
    print("The result is", _usr_output(_usr_input), ".\n")

def bin_dec():
    _usr_input = int(input("\nBinary: "), 2)
    print("The result is", _usr_input, ".\n")

def dec_hex():
    _usr_input = int(input("\nDecimal: "))
    _usr_output = "{0:X}".format(_usr_input)
    print("The result is", _usr_output, ".\n")

def hex_dec():
    _usr_input = int(input("\nHexadecimal: "), 16)
    print("The result is", _usr_input, ".\n")

def bin_hex():
    _usr_input = int(input("\nBinary: "),2)
    _usr_output = "{0:X}".format(_usr_input)
    print("The result is", _usr_output, ".\n")

def hex_bin():
    _usr_input = int(input("\nHexadecimal: "),16)
    _usr_output = "{0:b}".format(_usr_input)
    print("The result is", _usr_output, ".\n")

exit_btn = False
while exit_btn == False:


    usr_intro = input("\nConvert from: (H)exadecimal, (B)inary or (D)ecimal\n")
    usr_result = input("Converting to: (H)exadecimal, (B)inary or (D)ecimal\n")

    if usr_intro == "H" or usr_intro == "h" and usr_result == "B"or usr_result == "b": hex_bin(); exit_btn = True
    elif usr_intro == "B" or usr_intro == "B" and usr_result == "H"or usr_result == "h": bin_hex(); exit_btn = True
    elif usr_intro == "D" or usr_intro == "d" and usr_result == "B"or usr_result == "b": dec_bin(); exit_btn = True
    elif usr_intro == "B" or usr_intro == "b" and usr_result == "D" or usr_result == "d": bin_dec(); exit_btn = True
    elif usr_intro == "D" or usr_intro == "d" and usr_result == "H"or usr_result == "h": dec_hex(); exit_btn = True
    elif usr_intro == "H" or usr_intro == "h" and usr_result == "D"or usr_result == "d": hex_dec(); exit_btn = True
    else: 
        print("Operation not valid")
        exit_btn = False
