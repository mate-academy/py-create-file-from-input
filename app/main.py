import re


def main() -> None:
    # filename = input("Enter name of the file: ")
    # filename = filename + ".txt"
    while True:
        filename = input("Enter name of the file: ")
        if re.fullmatch(r"\w{1,20}", filename):
            break
        print("❌ Invalid filename. Use only letters,"
              " numbers, and underscores (_).")
    filename += ".txt"

    with open(filename, "a") as f:

        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main()
