def main():
    with open(f"{input('Enter name of the file: ')}.txt", "w") as f:
        while True:
            match input("Enter new line of content: "):
                case "stop":
                    break
                case line:
                    f.write(f"{line}\n")


if __name__ == "__main__":
    main()
