def main() -> None:
    name = input("Enter name of the file: ")
    list_row = []
    while True:
        next_row = input("Enter new line of content: ")
        if next_row != "stop":
            list_row.append(next_row)
        else:
            with open(f"{name}.txt", "w", newline="", encoding="utf-8") as f:
                for word in list_row:
                    f.write(word + "\n")
            break


if __name__ == "__main__":
    main()
