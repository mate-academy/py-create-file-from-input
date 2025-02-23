def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    res = []
    sentence = input("Enter new line of content: ")
    while sentence != "stop":
        res.append(sentence)
        sentence = input("Enter new line of content: ")

    with open(file_name, "w", encoding="utf-8") as file:
        w_res = "\n".join(res)
        file.write(w_res)


if __name__ == "__main__":
    main()
