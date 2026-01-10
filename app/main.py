def main() -> None:
    file_name = input("Enter name of the file: ")
    if file_name[-4] != ".txt":
        file_name += ".txt"

    with open(file_name, mode="w") as file_out:

        while True:
            user_prompt = input("Enter new line of content: ")

            if user_prompt == "stop":
                break

            file_out.write(user_prompt + "\n")
