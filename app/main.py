def main():
    file_name = input("Enter name of the file: ")
    print(file_name)
    output_file = open(f"{file_name}.txt", "a")

    while True:
        temp_input = input("Enter new line of content: ")
        print(temp_input)
        if temp_input == "stop":
            break
        output_file.write(f"{temp_input}\n")
    output_file.close()


if __name__ == "__main__":
    main()
