def main() -> None:
    name = input("Enter name of the file: ")
    content = ""
    with open(f"{name}.txt", "a") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            f.write(f"{content}\n")

    with open(f"{name}.txt", "r") as f:
        print(f'File name: "{name}.txt"')
        print("File content:")
        print(f.read())


if __name__ == "__main__":
    main()
