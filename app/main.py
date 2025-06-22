def main() -> None:
    file_name = input("write name of the file_result")
    file_name = file_name + ".txt"
    file_result = open(file_name, "w")
    while True:
        user_input = input()
        if user_input.strip().lower() == "stop":
            file_result.close()
            break
        file_result.write(user_input)
        file_result.write("\n")
    file_result.close()


if __name__ == "__main__":
    main()
