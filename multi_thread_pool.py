import threadpool
import time

def say_hello(a):
    print(f"hello:{a}")
    time.sleep(2)

def main():
    global result
    seed = ["a","b","c"]
    start = time.time()
    task_pool = threadpool.ThreadPool(5)
    requests = threadpool.makeRequests(say_hello,seed)
    for req in requests:
        task_pool.putRequest(req)
    task_pool.wait()
    end = time.time()
    time_m = end-start
    print(f"time:{time_m}")
    start1 = time.time()
    for each in seed:
        say_hello(each)
    end1 = time.time()
    print(f"time1:{end1-start1}")


if __name__ == '__main__':
    main()