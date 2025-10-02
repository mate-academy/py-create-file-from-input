def main() -> None:
    name = input("Enter name of the file: ")
    sentence_lst = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            sentence_lst.append(line)
    with open(name + ".txt", "w") as file:
        for sentence in sentence_lst:
            file.write(sentence + "\n")

        # file.write("\n".join(sentence_lst))


if __name__ == "__main__":
    main()
