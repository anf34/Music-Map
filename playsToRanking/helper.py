def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)  # Iterate through lines and count them
        return line_count
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
