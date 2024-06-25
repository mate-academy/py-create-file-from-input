def main():
    file_name = input("Enter name of the file: ")
    lines = []
    while "stop" not in lines:
        lines.append(input("Enter new line of content: "))
    del lines[-1]
    with open(f"{file_name}.txt", "w") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
