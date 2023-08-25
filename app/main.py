def main() -> None:
    name = input("Enter name of the file: ")
    fil_e = open(f"{name}.txt", "w")
    while True:
        command = input("Enter new line of content: ")
        if command != "stop":
            fil_e.write(command + "\n")
        else:
            break
    fil_e.close()


if __name__ == "__main__":
    main()
