from sha_256 import generate_hash

def check_thumbprint():
    with open('kse.ua.der', 'rb') as file: # rb = read binary
        read_bytes = bytearray(file.read())
        
    result = generate_hash(read_bytes)
    change_to_upper = result.hex().upper()
    edited_format_thumbprint = ':'.join(change_to_upper[i:i+2] for i in range(0, len(change_to_upper), 2)) # Правильне форматування (взято з Gemini)

    print(f"Result of thumbprint: {edited_format_thumbprint}")

if __name__ == '__main__':
    check_thumbprint()