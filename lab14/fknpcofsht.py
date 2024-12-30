
def shift_lines_down(file_path, new_line):
    with open(file_path, 'r+b') as file:
        content = file.read()
        new_line_bytes = new_line.encode('utf-8')
        
        total_size = len(content)
        new_size = total_size + len(new_line_bytes)
        file.seek(0, 2)
        file.write(b'\x00' * (new_size - total_size))

        file.seek(len(new_line_bytes))
        file.write(content)

        file.seek(0)
        
        file.write(new_line_bytes)

if __name__ == "__main__":
    pass