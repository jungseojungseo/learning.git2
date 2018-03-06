# -*- coding: utf-8 -*-
def year(input_year):
    if (input_year % 4) == 0:
        if (input_year % 100) == 0:
            if (input_year % 400) == 0:
                return '윤년'
                    
            return '평년'
            
            
        return '윤년'
        
    
    else:
        return '일반년'
        



print year(2300)
