import asyncio

from hw4_sync import summ_sync, test_array
from hw4_async import summ_async
from hw4_multiproc import summ_multiproc
from hw4_thread import summ_threads


if __name__ == '__main__':
    print(f'Sync: {summ_sync(test_array)}')

    print(f'Threads: {summ_threads(test_array)}')

    print(f'Multiproc: {summ_multiproc(test_array)}')

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(summ_async(test_array))
    print(f'Async: {result}')




