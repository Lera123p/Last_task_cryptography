import os
import multiprocessing # Gemini підказав, яку можна бібліотеку використати для роботи з процесами, запущених на ядрах процесора
from sha_256 import generate_hash

def search_prefix(init_message, end_searching, end_result):
    bytes_array = bytearray(init_message, 'utf-8') # Перетворюємо наше повідомлення на масив байтів
    
    # Шукаємо префікс доти, поки процес не буде зупинено (допоки ми не знайдемо ціль у вигляді восьми нулів)
    while not end_searching.is_set():
        init_random_prefix = bytearray(os.urandom(20)) # Виділяємо сталу довжину префіксу = 20

        text_concatenation = init_random_prefix + bytes_array # Зліплюємо рандомно згенерований префікс і наш текст

        result_bytes = generate_hash(text_concatenation) # Використовуємо функцію з файлу "sha_256.py"

        result_text = result_bytes.hex() # Перетворення з байтів в текст (виправлено назву змінної)
 
        if result_text.startswith('00000000'):
            end_searching.set() # Ціль досягнута = процес подальшого пошуку зупинений

            end_result.put((init_random_prefix.hex(), result_text)) # Знайдений цільовий префікс + геш
            return

if __name__ == '__main__':
    init_message = "give my friend 2 bitcoins for a pizza"
    counting_cores = multiprocessing.cpu_count() # Пошук кількості ядер процеса
    
    manager = multiprocessing.Manager() #Manager зберігає оригінали змінних і роздає ядрам доступ до них (Gemini підказав найбільш гнучкий варіант організації процесів)

    end_searching = manager.Event() # Створення івенту через Manager

    end_result = manager.Queue()    # Створення черги через Manager
    
    print(f"Starting of searching prefix by {counting_cores} cores... Please, wait and keep calm...")

    processes = []
    
    # Функція, щоб пройтись по кожному ядру
    for core_number in range(counting_cores):
        all_main_arguments = (init_message, end_searching, end_result)
        new_process = multiprocessing.Process(target=search_prefix, args=all_main_arguments)
        processes.append(new_process)
        new_process.start()
        
    for process in processes:
        process.join() # Чекаємо допоки один процес не завершить роботу
        
    if not end_result.empty():
        end_prefix, end_hash = end_result.get()
        print("Goal prefix was founded :)")
        print(f"Goal prefix (hex): {end_prefix}")
        print(f"End result of hash: {end_hash}")