def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    content = []
    while True:
        text = input("Enter new line of content: ")

        if text == "stop":
            break
        content.append(text)

    with open(filename, "w") as f:
        for line in content:
            f.write(line + "\n")


# def main() -> None:
#     filename = input("Enter name of the file: ") + ".txt"
#     while True:
#         text = input("Enter new line of content: ")
#
#         if text != "stop":
#             f = open(filename, "w")
#             f.write(text + "\n")


if __name__ == "__main__":
    main()
