def main():
    file_name = input(
       "Enter name of the file: "
    ).strip()
    if not file_name:
        print("file name can't be empty. Program complete")
        return

    if not file_name.lower().endswith(".txt"):
        file_name += ".txt"

    print("Enter new line of content (type 'stop' to finish):")

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(file_name, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"File '{file_name}' has been created successfully.")
    print(f"Number of lines written: {len(lines)}")


if __name__ == "__main__":
    main()
