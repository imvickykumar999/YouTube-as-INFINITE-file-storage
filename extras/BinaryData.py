
def file_to_binary_string(file_path):
    with open(file_path, 'rb') as file:
        binary_code = file.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_code)
    return binary_string

def binary_string_to_file(binary_string, file_path):
    with open(file_path, 'wb') as file:
        bytes_list = [int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)]
        bytes_arr = bytearray(bytes_list)
        file.write(bytes_arr)


file_path = 'TVglitch.mp3'
binary_string = file_to_binary_string('Original/' + file_path)

with open('temp.txt', 'w') as f:
    f.write(binary_string)

with open('temp.txt', 'r') as f:
    binary_string = f.read()

binary_string_to_file(binary_string, 'Binary/' + file_path)
