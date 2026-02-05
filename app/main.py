def main() -> None:
    f_name = input("Enter name of the file: ")
    if ".txt" not in f_name:
        f_name = f_name + ".txt"
    with open(f_name, "w") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            f.write(text + "\n")


if __name__ == "__main__":
    main()
