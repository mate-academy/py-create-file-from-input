def main() -> None:
    name = input("Enter name of the file: ")
    result = []
    while True:
        word = input("Enter new line of content: ")
        if word == "stop":
            break
        else:
            result.append(word)
    print(result)
    with open(f"{name}.txt", "a") as f:
        f.writelines(line + "\n" for line in result)


if __name__ == "__main__":
    main()
