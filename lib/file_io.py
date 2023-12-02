from pathlib import Path

def write_file(file_name, file_content):
    # Convert PosixPath object to string
    file_name = str(file_name)
    
    # Add the file extension to the file_name
    file_name_with_extension = file_name + ".txt"

    # Open the file in write mode and write the content
    with open(file_name_with_extension, "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Convert PosixPath object to string
    file_name = str(file_name)
    
    # Add the file extension to the file_name
    file_name_with_extension = file_name + ".txt"

    # Open the file in append mode and append the content
    with open(file_name_with_extension, "a") as file:
        file.write("\n" + append_content)

def read_file(file_name):
    # Convert PosixPath object to string
    file_name = str(file_name)
    
    # Add the file extension to the file_name
    file_name_with_extension = file_name + ".txt"

    # Open the file in read mode and read the content
    with open(file_name_with_extension, "r") as file:
        content = file.read()
    
    return content
