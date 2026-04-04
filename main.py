from buddy import Buddy


def main():
    buddy = Buddy(name="Friend")

    print(buddy.greet())
    print()
    print(buddy.daily_tip())
    print()
    print(buddy.stats())


if __name__ == "__main__":
    main()
