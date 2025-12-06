def main() -> None:
    file_name = input("Enter name of the file: ")
    open(f"{file_name}.txt", "w").close()

    with open(f"{file_name}.txt", "a") as file:
        user_response = ""
        while user_response != "stop":
            user_response = input("Enter new line of content: ")
            if user_response == "stop":
                break
            file.write(f"{user_response}\n")


if __name__ == "__main__":
    main()
