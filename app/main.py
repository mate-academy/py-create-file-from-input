def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "w") as f:
        while True:
            userstr = input("Enter new line of content: ")
            if userstr == "stop":
                break
            f.write(userstr + "\n")


if __name__ == "__main__":
    main()
