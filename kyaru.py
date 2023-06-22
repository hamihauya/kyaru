from os import system

class Character:
    def __init__(self, health):
        self.health = health

if __name__ == "__main__":
    system("cls")
    print("캬루괴롭히기게임")
    print("")
    print("1) 게임시작")
    print("")
    input(">> ")
    system("cls")

    kyaru = Character(20)
    print("캬루가 자고있어요.")
    print("")
    while(True):
        print("캬루의체력: " + str(kyaru.health))
        print("")
        if kyaru.health <= 0:
            print("캬루죽었어요...")
            print("")
            break
        elif kyaru.health >= 100:
            print("카루가 이제는 배불렀는지")
            print("배신해버리네요...")
            print("")
            break
        print("1) 캬루쓰다듬기 (체력 +1)")
        print("2) 캬루때리기 (체력 -1)")
        print("3) 캬루버리기")
        print("")
        choice = input(">> ")
        system("cls")
        if choice == "1":
            print("캐르릉~ 기분좋아요!")
            print("")
            kyaru.health += 1
        elif choice == "2":
            print("캐흐흑... 캬루 너무아파요ㅠㅠ")
            print("")
            kyaru.health -= 1
        elif choice == "3":
            print("카루가 미워한대요...")
            print("")
            break
        else:
            print("올바르지않는명령어에요.")
            print("")
        continue
    system("pause")
