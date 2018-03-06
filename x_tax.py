# -*- coding: utf-8 -*-
def tax(age, money, baby):
    if age >= 16 and age <= 65:
        if money <= 20000:
            if baby == 1:
                return money * 0.2 * 0.9
            else:
                return money * 0.2
        elif baby == 1:
            return money * 0.5 * 0.9
        else:
            return money * 0.5
        
    else:
        return 0



if __name__ == "__main__":
    print tax(20, 50000, 0)
