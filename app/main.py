def main() -> None:
    filename = input("Enter name of the file: ")
    filename += ".txt"
    with open(filename, "w") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop" or content == "":
                break
            f.write(f"{content}\n")


if __name__ == "__main__":
    main()
