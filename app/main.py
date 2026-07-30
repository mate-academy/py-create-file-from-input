def main():
    file_basename = input("Enter name of the file: ")
    with open(f"{file_basename}.txt", "a") as f:
        while True:
            user_content = input("Enter new line of content: ")
            if user_content == "stop":
                break
            f.write(f"{user_content}\n")


if __name__ == "__main__":
    main()
