import time

def elapsed(original_func):
    def warpper():
        start = time.time()
        result = original_func()
        end = time.time()
        print("함수 수행 시간: %f초" %(end - start))
        return result
    return warpper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

myfunc()