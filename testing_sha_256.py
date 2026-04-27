from sha_256 import generate_hash 

def testing_nist_vectors():
    test_vectors = [
        (
            "", # базовий Padding
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        ),
        (
            "abc", 
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
        ),
        (
            "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq", 
            "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1"
        )
    ]

    test_number = 1 # Лічильник для нумерації тестів

    for t in test_vectors:
        text_message = t[0] # Перший елемент - це текст
        correct_hash = t[1] # Другий елемент - це правильний хеш
        result = generate_hash(text_message)
        calculated_hash = result.hex()
     
        if calculated_hash == correct_hash:
            printed_result = "hashes are equal :)"
        else:
            printed_result = "hashes are not equal :("
        
        if text_message == "":
            printed_message = "Empty string"
        else:
            printed_message = f"'{text_message}'"
        
        print(f"Testing of #{test_number}: {printed_result}")
        print(f"Initial data: {printed_message}")
        print(f"Got: {calculated_hash}")
        print(f"Expected: {correct_hash}")
    
        test_number = test_number + 1

if __name__ == "__main__":
    testing_nist_vectors()