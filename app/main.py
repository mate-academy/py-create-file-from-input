def main():
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    print("To save and exit print stop")

    with open(file_name, 'w') as f:
        while True:
            input_str = input("Enter new line of content: ")
            if input_str == "stop":
                break
            f.write(input_str + "\n")



if __name__ == "__main__":
    main()
