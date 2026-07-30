def main() -> None:
    content_list = []
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            else:
                content_list.append(content + "\n")
        f.write("".join(content_list))
        f.close()


if __name__ == "__main__":
    main()
