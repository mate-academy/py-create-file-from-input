import os


def main(user_file_path: str = None) -> None:
    if user_file_path is None:
        enter_file_name = input("Enter name of the file: ")
        if len(enter_file_name.strip()) == 0:
            raise ValueError("Enter file name!")

        user_file_name = f"{enter_file_name}.txt"
        current_dir = os.path.dirname(__file__)
        data_dir = os.path.join(current_dir, "..")
        os.makedirs(data_dir, exist_ok=True)
        user_file_path = os.path.join(data_dir, user_file_name)

    with open(user_file_path, "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line.strip().lower() == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main()
