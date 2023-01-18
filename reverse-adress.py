# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reverse-adress.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/17 12:06:58 by sbelondr          #+#    #+#              #
#    Updated: 2023/01/18 08:58:09 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pyperclip

def transform(addr):
    # remove 0x
    if addr[:2] == "0x":
        addr = addr[2:]

    len_addr = len(addr)

    # add 0
    if len_addr % 2 != 0:
        len_addr += 1
        addr = '0' + addr

    value = ""
    for i in range(len_addr - 1, 0, -2):
        value += "\\x" + addr[i - 1] + addr[i]
    
    value = "'%s'" % (value)

    print("\033[94m")
    print(value)
    print("\033[0m")

    pyperclip.copy(value)
    print("✅ Buffer is copied in your clipboard")


def get_value():
    addr = input("Enter address: ")

    return addr

def main():
    addr = get_value()
    transform(addr)

    #int_addr = int(addr, 16)
    #total = hex(int_addr + 4)
    #addr_hex = str(total)[2:]
    #print("\nAddress + 4 (0x%s):" % (addr_hex))
    #transform(addr_hex)


if __name__ == "__main__":
    main()
