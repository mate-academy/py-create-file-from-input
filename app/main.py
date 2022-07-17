def main():
    filename = input("Enter name of the file: ")
    new_line_content = ""
    while new_line_content != "stop":
        new_line_content = input("Enter new line of content: ")
        with open(f"{filename}.txt", "a") as f:
            f.write(f"{new_line_content}\n")

    with open(f"{filename}.txt") as f:
        a = f.readlines()
        a.remove("stop\n")
        b = "".join(a)

    with open(f"{filename}.txt", "w") as f:
        f.write(f"{b}")


if __name__ == "__main__":
    main()
