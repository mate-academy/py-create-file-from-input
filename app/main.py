def main() -> None:
    file_name = ""
    while not file_name:
        file_name = input("Enter name of the file: ").strip()
    if not file_name.lower().endswith(".txt"):
        file_name += ".txt"
    with open(file_name, "w") as file:
        while True:
            content_request = input("Enter new line of content: ")
            if content_request.lower() == "stop":
                break
            file.write(f"{content_request}\n")


if __name__ == "__main__":
    main()
