def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    line = []
    with open(file_name, "w") as f:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                break
            line.append(user_input)
        f.write("\n".join(line))


if __name__ == "__main__":
    main()
