'''Style            Color              Back
0: None             30: White          40: White
1: Bold             31: Red            41: Red
4: Underline        32: Green          42: Green
7: Inverse          33: Yellow         43: Yellow
                    34: Blue           44: Blue
                    35: Magenta        45: Magenta
                    36: Cyan           46: Cyan
                    37: Light Gray     47: Light Gray'''

print('\033[4;32mOlá Mundo!\033[m')

red = '\033[1;31m'
green = '\033[1;32m'
end = '\033[m'

print(f'{red}Olá Mundo{green}!!!{end}')
