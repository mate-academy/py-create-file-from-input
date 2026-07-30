def main():
    name_of_file = input("Enter name of the file: ")
    result = []
    while True:
        content_of_file = input("Enter new line of content: ")
        if content_of_file == "stop":
            break
        else:
            result.append(content_of_file)
    with open(f"{name_of_file}.txt", "w") as f:
        for element in result:
            f.write(f"{element}\n")


if __name__ == "__main__":
    main()
