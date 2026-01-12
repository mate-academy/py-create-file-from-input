def main():
    file_name = input("Enter name of the file: ")
    user_stop = True
    user_lines = []

    while user_stop:
        user_new_line = input("Enter new line of content: ")
        if user_new_line == "stop":
            user_stop = False
            break
        user_lines.append(user_new_line)

    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(user_lines))


if __name__ == "__main__":
    main()
