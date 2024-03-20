import multiprocessing

from HW4.hw4_sync import calculate_time, test_array

summ = multiprocessing.Value('i', 0)

PROCS = 7


@calculate_time
def summ_multiproc(user_array):
    multiprocess = []
    for i in range(PROCS):
        STEP=len(user_array) // PROCS
        start_num = i * STEP
        end_num = start_num + STEP
        if i+1 == PROCS:
            end_num=len(user_array)
        t = multiprocessing.Process(target=process_summ, args=(user_array, start_num, end_num, summ, ))
        multiprocess.append(t)


    for t in multiprocess:
        t.start()
        t.join()

    return summ.value


def process_summ(user_array, start_num, end_num, summ):

    for i in range(start_num, end_num):
        with summ.get_lock():
            summ.value += user_array[i]

if __name__ == '__main__':

    print(f'Multiproc: {summ_multiproc(test_array)}')
    print(sum(test_array))