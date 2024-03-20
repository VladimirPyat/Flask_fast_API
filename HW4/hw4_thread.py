import threading

from HW4.hw4_sync import calculate_time, test_array


summ = 0
THREADS = 7


@calculate_time
def summ_threads(user_array):
    threads = []
    for i in range(THREADS):
        STEP=len(user_array) // THREADS
        start_num = i * STEP
        end_num = start_num + STEP
        if i+1 == THREADS:
            end_num=len(user_array)
        t = threading.Thread(target=process_summ, args=(user_array, start_num, end_num,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return summ


def process_summ(user_array, start_num, end_num):
    global summ
    for i in range(start_num, end_num):

        summ += user_array[i]


if __name__ == '__main__':

    print(f'Threads: {summ_threads(test_array)}')
    print(sum(test_array))
