def main():
    file_name = input("Enter name of the file: ")
    input_list = []
    while True:
        inp = input("Enter new line of content: ")
        if inp == "stop":
            break
        input_list.append(inp)
    content = "\n".join(input_list)
    with open(f"{file_name}.txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
