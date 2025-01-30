def main() -> None:
    # write your code here
    name = input("Enter name of the file: ")
    while 1 :
        with open(f"{name}.txt", "a") as fi:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            else:
                fi.write(f"{line}\n")


if __name__ == "__main__":
    main()
