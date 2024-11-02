def main() -> None:
    # write your code here
    f_name = input("Enter name of the file: ")
#    f_name = f_name[:f_name.find(".")] if f_name.find(".") else f_name
    f_name = f"{f_name}.txt"

    new_line = None
    with open(f_name, "a") as stream:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            stream.write(new_line + "\n")

        stream.close()
    return


if __name__ == "__main__":
    main()
