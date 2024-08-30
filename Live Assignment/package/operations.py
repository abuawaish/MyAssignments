# file_operations.py

def read_file(file_path):
    """
    Reads the contents of a file and returns it as a string.
    
    :param file_path: Path to the file to be read.
    :return: Contents of the file as a string.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

def write_file(file_path, data):
    """
    Writes data to a file. Overwrites the file if it already exists.
    
    :param file_path: Path to the file to be written to.
    :param data: Data to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except Exception as e:
        return f"An error occurred while writing to the file: {e}"
    return "Data written successfully."

def append_to_file(file_path, data):
    """
    Appends data to a file. Creates the file if it does not exist.
    
    :param file_path: Path to the file to be appended to.
    :param data: Data to be appended to the file.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(data)
    except Exception as e:
        return f"An error occurred while appending to the file: {e}"
    return "Data appended successfully."

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Define file path
    file_path = 'example.txt'
    
    # Write data to file
    write_result = write_file(file_path, "Hello, World!\n")
    print(write_result)
    
    # Append data to file
    append_result = append_to_file(file_path, "This is a new line.\n")
    print(append_result)
    
    # Read data from file
    read_result = read_file(file_path)
    print(f"File contents:\n{read_result}")
