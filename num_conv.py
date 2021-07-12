#This program is a number converter. Transforms numbers into binary and hexadecimal.
 
def dec_bin():
    _usr_input = int(input("\nDecimal: "))
    _usr_output = "{0:b}".format(_usr_input)
    print(f"The result is {_usr_output}.\n")  

def bin_dec():
    _usr_input = int(input("\nBinary: "), 2)
    print(f"The result is {_usr_input}.\n")

def dec_hex():
    _usr_input = int(input("\nDecimal: "))
    _usr_output = "{0:X}".format(_usr_input)
    print(f"The result is {_usr_output}.\n")

def hex_dec():
    _usr_input = int(input("\nHexadecimal: "), 16)
    print(f"The result is {_usr_input}.\n")

def bin_hex():
    _usr_input = int(input("\nBinary: "),2)
    _usr_output = "{0:X}".format(_usr_input)
    print(f"The result is {_usr_output}.\n")

def hex_bin():
    _usr_input = int(input("\nHexadecimal: "),16)
    _usr_output = "{0:b}".format(_usr_input)
    print(f"The result is {_usr_output}.\n")

exit_btn = False
while exit_btn == False:


    usr_intro = input("\nConvert from: (H)exadecimal, (B)inary or (D)ecimal\n").capitalize()
    usr_result = input("Converting to: (H)exadecimal, (B)inary or (D)ecimal\n").capitalize()

    if usr_intro == "H" and usr_result == "B": 
      hex_bin() 
      exit_btn = True
    elif usr_intro == "B" and usr_result == "H": 
      bin_hex() 
      exit_btn = True
    elif usr_intro == "D" and usr_result == "B": 
      dec_bin() 
      exit_btn = True
    elif usr_intro == "B" and usr_result == "D": 
      bin_dec() 
      exit_btn = True
    elif usr_intro == "D" and usr_result == "H": 
      dec_hex() 
      exit_btn = True
    elif usr_intro == "H" and usr_result == "D": 
      hex_dec() 
      exit_btn = True
    else: 
      print("Operation not valid")
      exit_btn = False
