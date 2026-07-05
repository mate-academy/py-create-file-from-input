def main() -> None:
    with open(f"{input('Enter name of the file: ')}.txt", "w") as uinput:
        while True:
            chunk = input("Enter new line of content: ")
            if chunk == "stop":
                break
            uinput.write(f"{chunk}\n")


if __name__ == "__main__":
    main()
