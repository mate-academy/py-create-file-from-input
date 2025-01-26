def main():
    sw_close = False
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while not sw_close:
            new_line = input("Enter new line of content: ")
            if new_line.lower() == "stop":
                sw_close = True
            else:
                file.writelines(f"{new_line}\n")


if __name__ == "__main__":
    main()
