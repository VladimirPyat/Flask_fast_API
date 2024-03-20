import asyncio

from HW4.hw4_sync import calculate_time, test_array

summ = 0
ASYNC_PROCS = 7


@calculate_time
async def summ_async(user_array):
    tasks = []
    global summ

    for i in range(ASYNC_PROCS):
        STEP=len(user_array) // ASYNC_PROCS
        start_num = i * STEP
        end_num = start_num + STEP
        if i+1 == ASYNC_PROCS:
            end_num=len(user_array)
        task = asyncio.create_task(process_summ(user_array, start_num, end_num))
        tasks.append(task)

    await asyncio.gather(*tasks)

    return summ


async def process_summ(user_array, start_num, end_num):
    global summ
    for i in range(start_num, end_num):

        summ += user_array[i]


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(summ_async(test_array))
    print(f'Async: {result}')
    print(sum(test_array))
