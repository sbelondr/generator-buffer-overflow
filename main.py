# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/16 14:06:44 by sbelondr          #+#    #+#              #
#    Updated: 2023/01/16 14:20:36 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from string import ascii_lowercase
import sys

def print_header():
    '''
    useless header
    '''
    print("\033[92m")
    print("====================== Buffer Overflow Generator ======================")

def generate_buffer():
    '''
    Generate new buffer
    Return:
         - buffer (str): new buffer
    '''
    print("\033[93m")
    test= input("\tLength: ")

    len_input = int(test) + 1
    sz = 0
    buffer = ""
    for i in ascii_lowercase:
        if sz > len_input:
            break
        for j in ascii_lowercase:
            if sz > len_input:
                break
            for n in range(0,10):
                if sz + 3 < len_input:
                    buffer += "%c%c%d" % (i.upper(), j, n)
                    sz += 3
                elif sz + 2 < len_input:
                    buffer += "%c%c" % (i.upper(), j)
                    sz += 2
                elif sz + 1 < len_input:
                    buffer += "%c" % (i.upper())
                    sz += 1
                else:
                    break

    print("\033[94m")
    print("------------------------------- Buffer -------------------------------")
    print(buffer)
    print("----------------------------------------------------------------------")
    return buffer

def input_get_eip():
    '''
    Get value of EIP with input user
    Return:
        - value_eip (str): eip value
    '''
    print("\033[93m")
    eip_value_hex=input("\tEnter EIP value: ")

    if eip_value_hex[:2] == "0x":
        eip_value_hex = eip_value_hex[2:]

    try:
        byte_array = bytearray.fromhex(eip_value_hex)
        value_eip = byte_array.decode()[::-1]
    except:
        print("\033[91m")
        print("Non-hexadecimal number", file=sys.stderr)
        print("\033[0m")
        exit(-1)

    print("\033[94m")
    print("\tValue decode is '%s'" % (value_eip))
    return value_eip

def calc_offset(buffer, value_eip):
    '''
    Calculate offset
    Args:
        - buffer (str): generate with generate_buffer function
        - value_eip (str): eip value
    '''
    try:
        offset = buffer.index(value_eip)
    except:
        print("\033[91m")
        print("Error: value not found", file=sys.stderr)
        print("\033[0m")
        exit(-1)

    print("\tOffset is '%d'" % (offset))
    print("\033[0m")

def main():
    print_header()
    buffer = generate_buffer()

    value_eip = input_get_eip()
    calc_offset(buffer, value_eip)

if __name__=="__main__":
    main()
