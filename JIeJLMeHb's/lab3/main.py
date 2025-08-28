import capsule as caps
import playstation_players as ps


def main():
    user_choice = int(input("Для функции логгирования выберите 1, для списка пользователей PS выберите 2: "))
    if user_choice == 1:
        caps.hello()
    if user_choice == 2:
        ps.main()

if __name__ == "__main__":
    main()
