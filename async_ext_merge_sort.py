import asyncio
import time
out_file = 'sorted.txt'
NumList = []
async def task(i):
    with open(out_file, 'w') as fout:
        for num in NumList:
            fout.write(str(num) + '\n')


async def main():

    in_files = ['unsorted_1.txt', 'unsorted_2.txt', 'unsorted_3.txt', 'unsorted_4.txt', 'unsorted_5.txt',
                'unsorted_6.txt', 'unsorted_7.txt', 'unsorted_8.txt',
                'unsorted_9.txt', 'unsorted_10.txt']

    for file in in_files:
        with open(file) as fin:
            for line in fin:
                NumList.append(int(line.strip()))
    coroutines = list()
    for i in range(len(NumList)):
        for j in range(1, len(NumList) - i):
            if NumList[j - 1] > NumList[j]:
                (NumList[j - 1], NumList[j]) = (NumList[j], NumList[j - 1])
    for i in NumList:
        coroutines.append(task(i))

    await asyncio.gather(*coroutines)

start = time.time()
asyncio.run(main())
time_file = open('async_time.txt','w')
time_file.write("program took "+ str(time.time() - start) +" to finish")
time_file.close()
