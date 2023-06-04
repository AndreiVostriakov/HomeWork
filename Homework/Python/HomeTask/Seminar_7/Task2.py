import time

def retry(max_retries):
    def decorator(func):
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except:
                    time.sleep(0.5)
        return _wrapper
    return decorator

@retry(5)
def greening():
    print("Как дела")
    raise Exception

greening()