import threading
import os
import time

MY_PATH = '.'


def count_words_in_file(file_):
    with open(file_, 'r', encoding='utf-8') as f:
        content = f.read()
        num_words = len(content.split())
        print(f'Слов в файле {file_}: {num_words}')


def process_files_in_directory(directory):
    threads = []

    for root, dirs, file_names in os.walk(directory):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            t = threading.Thread(target=count_words_in_file, args=(file_path,))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    start_time = time.time()
    process_files_in_directory(MY_PATH)

    print(f'Время выполнения {(time.time() - start_time):.2f}')