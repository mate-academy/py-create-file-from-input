def main() -> None:
    file_write = open(f"{input("Enter name of the file: ")}.txt", "w")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            file_write.write(line + "\n")
    file_write.close()


if __name__ == "__main__":
    main()
