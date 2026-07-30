def main() -> None:
    name = input("Enter name of the file: ").strip()
    if not name.endswith(".txt"):
        name += ".txt"
    line_list = []
    while True:
        sentence = input("Enter new line of content: ")
        if sentence == "stop":
            break
        line_list.append(sentence + "\n")

    with open(name, "w") as file:
        file.writelines(line_list)


if __name__ == "__main__":
    main()
