def main() -> None:
    app_name = input("Enter name of the file: ")
    with open(
            f"{app_name}.txt",
            "w",
            encoding="utf-8"
    ) as data_file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                return
            data_file.write(f"{text}\n")


if __name__ == "__main__":
    main()
