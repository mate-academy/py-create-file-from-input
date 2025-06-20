def main() -> None:
    file_name = input("Enter name of the file: ")
    fw = open(f"{file_name}.txt", "w")

    while True:
        input_string = input("Enter new line of content: ")
        if input_string != "stop":
            fw.write(f"{input_string}\n")
        # elif input_string == "":
        #     continue
        else:
            break

    fw.close()


if __name__ == "__main__":
    main()
