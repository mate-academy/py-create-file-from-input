def main():
    filename = input("Enter name of the file: ").strip()
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    full_filename = f"{filename}.txt"
    try:
        with open(full_filename, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
        print(f'File "{full_filename}" created successfully.')
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")


if __name__ == "__main__":
    main()
