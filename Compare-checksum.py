def main():
    val1 = ""
    val2 = ""

    val1 = input("Enter the first value to compare: ")
    val2 = input("Enter second value to compare: ")

    if val1 == val2:
        print("Match")
    else:
        print("No match")

    restart = input("Search again? [Y/N]: ").upper()
    if restart== "Y":
        main()
    else:
        quit()

if __name__ == "__main__":
    main()