"""装饰器__函数前处理和后处理"""
import functools
from typing import Callable
def data_processing_decorator(preprocess:Callable|None = None, postprocess:Callable|None = None):
    """
    一个装饰器，用于在函数调用前后处理数据
    :param preprocess: 一个函数，用于在原函数调用前处理输入数据。
    :param postprocess: 一个函数，用于在原函数调用后处理输出数据。
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 预处理输入数据
            if preprocess is not None:
                print(f"调用 {func.__name__} 前用{preprocess.__name__}处理输入数据\n")
                print(f"输入数据: {args}, {kwargs}\n")
                args = preprocess(*args)
            # 调用原函数
            result = func(*args, **kwargs)
            # 后处理输出数据
            if postprocess is not None:
                print(f"原函数返回数据: {result}\n")
                print(f"调用 {func.__name__} 后用{postprocess.__name__}处理返回数据\n")
                result = postprocess(result)
            return result
        return wrapper
    return decorator


if __name__ == '__main__':
    # 示例的预处理和后处理函数
    def pre_process(*args):
        '''假设输入是一个整数列表，我们将每个元素加1'''
        return [arg + 1 for arg in args]

    def post_process(result):
        '''假设输出是一个整数，我们将其乘以2'''
        return result * 2

    @data_processing_decorator(
        preprocess=pre_process,
        postprocess= post_process
    )
    def my_function(x, y, z):
        '''将x, y, z的元素相加'''
        return x + y + z

    # 调用装饰后的函数
    RESULT = my_function(1, 2, 3)
    print(RESULT)  # 输出应该是14 (预处理: [2, 3, 4], 原函数计算: 2+3+4=9, 后处理: 9*2=18)
