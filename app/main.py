def main() -> None:
    """
        Collects user input line by line and writes it to a file,
        ensuring each input line appears on a separate line in the file.
        """

    file_name = input("Enter name of the file: ")

    if not file_name:
        print("File name cannot be empty. Exiting.")
        return

    comments = []
    print("\nStart entering content. "
          "Type 'stop' (case-insensitive) to finish.")

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        else:
            comments.append(line)

    try:
        with open(file_name + ".txt", "w") as file:
            for comment in comments:
                file.writelines(comment + "\n")
    except Exception as e:
        print("Something went wrong:", e)


if __name__ == "__main__":
    main()
