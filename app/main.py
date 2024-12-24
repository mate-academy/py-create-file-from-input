def main():
    # write your code here
    name = input("Enter name of the file: ") + ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    with open(f"{name}", "w") as f:
        f.write(f"File name: {name}\n")
        f.write(f"File content:\n")
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
