import time, logging
from functools import wraps
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="logs_file.log",
    encoding="utf-8",
    level = logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')

def log_call(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            logger.info(f"Function '{func.__name__}' start")
            logger.info(func(*args, **kwargs))
            logger.info(f"Function '{func.__name__}' end")
        except Exception as e:
            logger.error(f"Function {func.__name__} call error {e}")

    return inner

def measure_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        working_time = end - start
        return working_time

    return inner

@log_call
@measure_time
def greeting(name):
    print(f"Hello, {name}")

@log_call
@measure_time
def testing():
    time.sleep(1)
    return "Done"


@log_call
@measure_time
def error():
    return "Check"

print(greeting("Kate"))
print(testing())
print(error("Hi"))
