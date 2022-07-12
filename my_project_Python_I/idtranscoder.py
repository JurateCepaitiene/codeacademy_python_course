import datetime
import string

def control_number(id_digits : list) -> int:
    list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    list1 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    control0 = 0
    control1 = 0
    for i in range(10):
        control0 = control0 + id_digits[i] * list0[i]
        control1 += id_digits[i] * list1[i]
    control0 = control0 % 11
    control1 %= 11
    result = 0
    if control0 != 10:
        result = control0
    elif control1 != 10:
        result = control1
    return result

def is_id_valid(id : string) -> bool:
    is_valid = False
    year = 0
    month = 0
    day = 0
    digits = []
    if len(id) == 11 and id.isdigit():
        digits = [int(n) for n in list(id)]
        if digits[0] == 9:
            is_valid = True
        elif digits[0] >= 1 and digits[0] <= 6:
            year = digits[1] * 10 + digits[2]
            month = digits[3] * 10 + digits[4]
            day = digits[5] * 10 + digits[6]

            if year == 0 and month == 0 and day == 0:
                is_valid = True        
            else:
                if digits[0] == 1 or digits[0] == 2:
                    year += 1800
                elif digits[0] == 3 or digits[0] == 4:
                    year += 1900
                elif digits[0] == 5 or digits[0] == 6:
                    year += 2000
                
                date_is_correct = True
                try:
                    date = datetime.datetime(year, month, day)
                except ValueError:
                    date_is_correct = False

                if date_is_correct:
                    control = control_number(digits)
                    if control == digits[10]:
                        is_valid = True
    return is_valid, year, month, day, digits


if __name__ == "__main__":
    id = input("Please enter your personal ID in format 12345678900: ")
    if is_id_valid(id) == True:
        print("All good")
    else:
        print("You fail")