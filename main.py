import itertools
from logger import logger, logger_with_path


@logger
def single_nested(iterable: list | tuple) -> tuple:
    try:
        flat = tuple(itertools.chain.from_iterable(iterable))
        return flat
    except Exception as ex:
        print('Error: Something went wrong!')


@logger_with_path(path_to_log='/Users/antonbannikov/Desktop/decorators')
def many_nested(iterable: list | tuple) -> tuple:
    try:
        flat = list(itertools.chain.from_iterable(iterable))
        if any(map(lambda x: type(x) == list, flat)) is True:
            flat = many_nested(flat)
        return tuple(flat)
    except Exception as ex:
        print('Error: Something went wrong!')


def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    any_nested_list = [
        [[['Beautiful', 'is', 'better'], ['than', 'ugly', '.']], [['Explicit', 'is', 'better'],
                                                                  ['than', 'implicit', '.']]],
        [[['Simple', 'is', 'better'], ['than', 'complex', '.']], [['Complex', 'is', 'better'],
                                                                  ['than', 'complicated', '.']]]
    ]

    single_nested(nested_list)
    many_nested(any_nested_list)


if __name__ == '__main__':
    main()
