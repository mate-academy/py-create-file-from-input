def main() -> None:
    user = input("Enter name of the file: ")
    filename = user + ".txt"
    lista = []
    while True:
        user2 = input("Enter new line of content: ")
        if user2 == "stop":
            break
        lista.append(user2 + "\n")
    with open(filename, "w") as file:
        file.writelines(lista)


if __name__ == "__main__":
    main()
