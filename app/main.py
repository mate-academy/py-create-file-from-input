def main():
    name = input("File name: ")

    if not name.endswith(".txt"):
        name += ".txt"

    with open(name, "w") as f:
        while True:
            file = input("file content: ")
            if file == "stop":
                break
            f.write(file + "\n")


if __name__ == "__main__":
    main()
