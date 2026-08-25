def create_file() -> None:
    file_name = input("Enter name of the file: ")
    normalized_file_name = f"{file_name}.txt"

    with open(normalized_file_name, "a") as f:
        stop_word = "stop"
        while True:
            line = input("Enter new line of content: ")
            if line == stop_word:
                break
            f.write(f"{line}\n")
