from program_files import value as v
from program_files import counter as c
from program_files import timelimit as t

def main():
    try:
        user_choice = int(input("Для многопотока введите 1," \
        " для многопроцессора введите 2," \
        " для timelimit введите 3: "))
    except ValueError:
        print("Идиот, введи число")
        main()
    except UnboundLocalError:
        pass
    try:
        if user_choice == 1:
            c.main()
        elif user_choice == 2:
            v.main() 
        elif user_choice == 3:
            t.main()
        else:
            print("Идиот, число от 1 до 3")
            main()
    except UnboundLocalError:
        pass    
        

if __name__ == "__main__":
    main()