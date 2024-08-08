'''将一段时间按固定的天数拆分成N个的一个装饰器'''
import datetime
from functools import wraps
def split_time_range_decorator(step = 7):
    """
    装饰器，将开始时间和结束时间按每7天分段，并依次调用目标函数
    """
    def decorator(func):
        @wraps(func)
        def wrapper(begintime, endtime, *args, **kwargs,):
            # 将字符串格式的时间转换为datetime对象
            start = datetime.datetime.strptime(begintime, '%Y-%m-%d %H:%M:%S')
            end = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
            # 分割时间区间并依次调用目标函数
            current_start = start
            while current_start < end:
                current_end = current_start + datetime.timedelta(days=step)
                if current_end > end:
                    current_end = end
                # 调用目标函数，并传递当前区间的开始时间和结束时间
                func(current_start.strftime('%Y-%m-%d %H:%M:%S'), current_end.strftime('%Y-%m-%d %H:%M:%S'), *args, **kwargs)
                current_start = current_end
        return wrapper
    return decorator




@split_time_range_decorator(step = 3)
def print_time_range(begintime, endtime):
    print('开始时间：%s，结束时间：%s' % (begintime, endtime))


print_time_range(begintime = '2021-01-01 00:00:00',endtime = '2021-01-31 23:59:59')
