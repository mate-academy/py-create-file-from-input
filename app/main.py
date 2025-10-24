def main(content: list, file_basename: str) -> None:
    # write your code here
    file_basename = input("Enter name of the file:")
    print(f"hello word {file_basename}")

    with open(f"{file_basename}.txt", "a") as f:
        while True:
            line = input("Enter new line of content:")
            if line == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main([], "")
