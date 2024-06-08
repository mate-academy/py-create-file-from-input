def main() -> object:
    file_name = input("Enter the file name: ")
    new_line = input("Enter next line of the content: ")
    with open(f"{file_name}.txt", "a") as f:
        while new_line != "stop":
            f.write(new_line)



if __name__ == "__main__":
    main()
