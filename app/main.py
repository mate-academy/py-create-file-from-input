def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    with open(filename, "a") as f:
        pass

    ss = []
    while True:
        row = input("Enter new line of content: ")
        if row == "stop":
            break
        ss.append(row)

    if ss:
        with open(filename, "w") as f:
            for i in ss[:-1]:
                f.write(i + "\n")
            f.write(ss[-1])
    else:
        print("Nothing to write to the file.")


if __name__ == "__main__":
    main()
