def main() -> None:
    user_file_name = input("Enter name of the file: ")
    file_name = f"{user_file_name}.txt"
    with open(file_name, "a") as f:
        lines = []
        while True:
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                break
            lines.append(user_input)
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
