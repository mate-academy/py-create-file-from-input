def main() -> None:
    input_name = input("Enter name of the file: ")
    with open(f"{input_name}.txt", "w") as f:
        stop = False
        while not stop:
            input_content = input("Enter new line of content: ")
            if input_content == "stop":
                stop = True
            else:
                f.write(f"{input_content}\n")


if __name__ == "__main__":
    main()
