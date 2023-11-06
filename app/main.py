def main():
    name_file = input("Enter name of the file: ")
    lines_arr = []
    while True:
        new_string = input("Enter new line of content: ")
        if new_string != "stop":
            lines_arr.append(new_string)
        else:
            break
    with open(f"{name_file}.txt", "a") as file:
        for line in lines_arr:
            file.write(f"{line}\n")

if __name__ == "__main__":
    main()
