def main() -> None:
    filename = input("Enter name of the file: ")
    res = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        res += f"{line}\n"
    with open(f"{filename}.txt", "a") as f:
        f.write(f"{res}")


if __name__ == "__main__":
    main()
