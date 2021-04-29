# def print_cube(num):
#     """
#     function to print cube of given num
#     """
#     print("Cube: {}".format(num * num * num))


# def print_square(num):
#     """
#     function to print square of given num
#     """
#     print("Square: {}".format(num * num))


# if __name__ == '__main__':

#     # creating processes
#     p1 = multiprocessing.Process(target=print_square, args=(10, ))
#     p2 = multiprocessing.Process(target=print_cube, args=(5, ))

#     # starting process 1
#     p1.start()
#     # starting process 2
#     p2.start()

#     # wait until process 1 is finished
#     p1.join()
#     # wait until process 2 is finished
#     p2.join()

#     # both processes finished
#     print("Done!")


# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return f'Done Sleeping...{seconds}'


# with concurrent.futures.ProcessPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = executor.map(do_something, secs)

#     # for result in results:
#     #     print(result)

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)')
# import concurrent.futures
# import time

from multiprocessing import Pool
from time import sleep

def f(x):
    sleep(4)
    return x*x


if __name__ == '__main__':
    with Pool(processes= 5) as p:
        
        a = p.map(f, [1, 2, 3])
    print(a)
