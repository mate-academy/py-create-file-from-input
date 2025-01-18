def main():
    enter_file_name = input("Enter file name: ")
    file_name = enter_file_name + ".txt"
    with open(file_name, "a") as f:
        enter_text = input("Enter next line: ")
        while enter_text != "stop":
            f.write(f"{enter_text}\n")
            enter_text = input("Enter next line: ")


if __name__ == "__main__":
    main()
