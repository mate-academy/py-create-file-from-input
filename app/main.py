def main() -> None:
    name = input("Enter name of the file: ")
    content = ""
    try:
        with open(f"{name}.txt", "w") as file_open:
            content = ""
            try:
                while True:
                    text = input("Enter new line of content: ")
                    if text == "stop":
                        raise AssertionError("stop")
                    content += text + "\n"
            except AssertionError:
                file_open.write(content)
                if text != "stop" or text is None:
                    content += "\n" + text
    except IndexError:
        pass


if __name__ == "__main__":
    main()
