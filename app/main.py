def main() -> None:
    name_fail = input("Enter name of the file: ") + ".txt"

    lines = []

    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        lines.append(user_input)

    with open(name_fail, "w") as obj_fail:
        obj_fail.write("\n".join(lines))


if __name__ == "__main__":
    main()
