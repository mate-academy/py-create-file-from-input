def main() -> None:
    name1 = input("Enter name of the file: ")
    list_of_inputs = []
    second_input = input("Enter new line of content: ")
    while second_input.lower() != "stop":
        list_of_inputs.append(second_input)
        second_input = input("Enter new line of content: ")
    name_of_file = f"{name1}.txt"
    with open(name_of_file, "w") as file:
        for sentence in list_of_inputs:
            file.write(sentence + "\n")


if __name__ == "__main__":
    main()
