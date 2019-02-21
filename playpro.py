roman_numerals = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}

def roman_int(user_choice):
    if user_choice == "1":
        user_roman = input("What numeral would you like to convert?\n").upper()
        resultI = 0
        for k,v in roman_numerals.items():          
            if user_roman == k:
                resultI += roman_numerals.get(user_roman)
            else:
                for i in user_roman:
                    if i in roman_numerals.keys():
                        if i == k:
                            resultI += v
    print(resultI)
