def main() -> None:
    # write your code here
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as f:
        while True:
            new_line = input("Enter new line of content: ").strip()
            if new_line.lower() == "stop":
                break
            f.write(new_line + "\n")


if __name__ == "__main__":
    main()
