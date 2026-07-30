def main() -> None:
    file_name = input("Enter name of the file: ")
    content_box = []
    while True:
        content = input("Enter new line of content: ")
        content_box.append(content)
        if content == "stop":
            content_box.pop(len(content_box) - 1)
            with open(f"{file_name}.txt", "w") as file:
                for element in content_box:
                    file.write(f"{element}\n")
            break
    pass


if __name__ == "__main__":
    main()
