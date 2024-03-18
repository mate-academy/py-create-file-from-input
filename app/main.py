def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}" + ".txt", "a") as file_write:
        while True:
            ask_to_add = input("Enter new line of content: ")
            if ask_to_add == "stop":
                break
            file_write.write(ask_to_add)
            file_write.write("\n")
    file_write.close()


if __name__ == "__main__":
    main()
