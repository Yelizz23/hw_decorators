from functools import wraps
from datetime import datetime
import os
from termcolor import colored, cprint


def color():
    cprint('Домашнее задание к лекции 3.«Decorators»:\n', 'red')
    text = colored('1. Написать декоратор - логгер.', 'magenta')

    print(text)
    cprint('2. Написать декоратор с параметром пути к логам.', 'magenta')

    coloured_homework = lambda x: cprint(x, 'magenta')
    coloured_homework('3. Применить написанный логгер к приложению из любого предыдущего д/з.')


color()


def logger(function):
    @wraps(function)
    def loggers(*args, **kwargs):
        with open('logs.txt', 'a') as file:
            file.write(datetime.now().strftime('%Y-%m-%d %H:%S:%f') + '\n')
            file.write(datetime.now().strftime('%Y-%m-%d %H:%S:%f') + '\n')
            file.write(f'The function name: \'{function.__name__}\', \n')
            file.write(f'arguments: {args}{kwargs},\n')
            result = function(*args, **kwargs)
            file.write(f'results {result}\n************************\n')
            return result
    return loggers


def logger_with_path(path_to_log):
    def logger_path(func):
        if not os.path.isdir(path_to_log):
            os.makedirs(path_to_log)
        step = True

        @wraps(func)
        def loggs(*args, **kwargs):
            nonlocal step
            if step:
                step = False
                with open(f'{path_to_log}/logs.txt', 'a') as file:
                    file.write(datetime.now().strftime('%Y-%m-%d %H:%S:%f') + '\n')
                    file.write(f'The function name: \'{func.__name__}\', \n')
                    file.write(f'arguments: {args}{kwargs},\n')
                    result = func(*args, **kwargs)
                    file.write(f'results{result}\n************************\n')
            else:
                result = func(*args, **kwargs)
                step = True
            return result
        return loggs
    return logger_path
