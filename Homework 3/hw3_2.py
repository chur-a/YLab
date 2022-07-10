from time import sleep

def repeat_func(call_count, start_sleep_time, factor, border_sleep_time):
    def decorator(func):
        def inner():
            i = 0
            t = start_sleep_time
            while i < call_count:
                print(f"Запуск номер {i+1}. Ожидание {t} секунд.")
                sleep(t)
                func()
                t *= pow(2, factor)
                if t > border_sleep_time:
                    t = border_sleep_time
                i += 1
        return inner
    return decorator


@repeat_func(3, 1, 2, 12)
def pass_func():
    pass


pass_func()


