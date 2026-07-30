def main() -> None:
    name = input("Enter name of the file: ")
    final_list = []
    while True:
        new_line = input("Enter new line of content: ")
        final_list.append(f"{new_line}\n")
        if new_line == "stop":
            break

    with open(f"{name}.txt", "w") as f:
        for elem in final_list[:-1]:
            f.write(elem)


if __name__ == "__main__":
    main()
