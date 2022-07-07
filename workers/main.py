# Sukurti programą, kuri:

# Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba (data būtų nustatoma automatiškai, pagal dabartinę datą).
# Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
# Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

# class Worker:
#     pass

# def do_smth() -> None:
#     name = input('please, enter your name: ')
#     birthday = input('please, enter your birthday: ')
#     occupation = input('please, enter your occupation: ')
#     salary = input('please, enter your salary: ')
#     start_date = input('please, enter your start date: ')
#     print(f'My personal info is: {name} - {birthday} - {salary} - {start_date} - {occupation}')

# if __name__ == '__main__':
#     do_smth()

# veikia !!

class Pakisti:

    @staticmethod
    def do_smth() -> None:
        name = input('please, enter your name: (format: YYY-MM-DD):')
        birthday = input('please, enter your birthday: ')
        occupation = input('please, enter your occupation: ')
        salary = input('please, enter your salary: ')
        start_date = input('please, enter your start date: (format: YYY-MM-DD): ')
        print(f'My personal info is: {name} - {birthday} - {salary} - {start_date} - {occupation}')

if __name__ == '__main__':
    Pakisti.do_smth()

# veikia !! Pakisa ta pati po klase, bet klases uzduoties pradziai isties nereikia


