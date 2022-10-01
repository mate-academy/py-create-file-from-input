def main():
    input_str = str(input("Enter name of the file: "))
    if input_str:
        file_name = input_str
        f = open(f"{file_name}.txt", "w")
        while True:
            input_str = str(input("Enter new line of content: "))
            if input_str != "stop":
                f.write(input_str + "\n")
            else:
                break
        f.close()


if __name__ == "__main__":
    main()
