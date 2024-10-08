def get_int_to_char_string(integer_value, desired_length):
    binary_number = bin(integer_value)[2:]
    # print(binary_number)
    # desired_length = 128

    # Count the length of the binary number
    current_length = len(binary_number)
    # print(current_length)

    # Add leading zeros if the length is less than the desired length
    if current_length < desired_length:
        binary_number = binary_number+'0' * (desired_length - current_length)

    binary_string = binary_number

    # Split the binary string into chunks of 8 bits
    binary_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    # Convert each binary chunk to its corresponding character
    character_string = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)
    # print(len(character_string))
    return character_string

    # print(character_string)  # Output: 'Hello'

