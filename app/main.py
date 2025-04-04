def main():
    file_name = input("Enter name of the file:")
    file_name += ".txt"

    content = []

    while True:
        line = input("Enter new line of content:")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")

    print(f"File '{file_name}' created successfully with the following content:")
    for line in content:
        print(line)



if __name__ == "__main__":
    main()
