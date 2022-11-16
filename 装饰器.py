import logging
import os
import sys
import time

'''
更新pip: pip3 install --upgrade pip -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
        python -m pip install --upgrade pip
        python -m pip install pywintypes -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

镜像网站:
http://mirrors.aliyun.com/pypi/simple/ 阿里云
https://pypi.mirrors.ustc.edu.cn/simple/  中国科技大学
http://pypi.douban.com/simple/  豆瓣
https://pypi.tuna.tsinghua.edu.cn/simple/ 清华大学
http://pypi.mirrors.ustc.edu.cn/simple/ 中国科学技术大学

:param func:出现的方法
python集成工具-Docstring-!plain
'''


def catch_except(func):
    '''
    应用于捕获异常并处理的装饰器
    :param func:
    :return:
    '''

    def wrapper(*args, **kwargs):
        '''
        函数的执行
        :param args:
        :param kwargs:
        :return:
        '''
        try:
            return func(*args, **kwargs)
        except NameError:  # 针对出错的例子
            print('数据不合法')
            # sys.exit()
        except KeyError:
            print('请确保取值在[0,1],并且element中有这个值')
            # sys.exit()
        except InputError as In:  # 自定义错误，矩阵阶数不同
            print(In)
            # sys.exit()
        except Exception as e:  # 系统错误
            print('warnning:', e)
            logging.warning(e)
            # sys.exit()

    return wrapper


class InputError(Exception):
    '''
    定义一个异常类,应用于 半hoop的判断.py 矩阵阶数不同
    '''

    def __init__(self, value):
        '''
            异常类型的说明信息
            :param value:
        '''
        # super.__init__(value)
        self.value = value

    def __str__(self):
        '''
        print 信息
        :return:
        '''
        return '{}的阶数与element数量不符，请检查'.format(repr(self.value))


def show_time(func):
    '''
    显示时间
    :param func:
    :return:
    '''

    def inner_func(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        ending = time.time()
        time_cost = ending - begin
        print('完成此项任务花费了 {} 秒'.format(time_cost))
        # print('it cost %f seconds'%(time_cost))
        return result

    return inner_func


def only_time(func):
    '''
    显示时间,不输出结果
    :param func:
    :return:
    '''

    def inner_func(*args, **kwargs):
        begin = time.time()
        with HiddenPrints() as f:
            result = func(*args, **kwargs)
        # print(f)
        ending = time.time()
        time_cost = ending - begin
        print('完成此项任务花费了 {} 秒'.format(time_cost))
        # print('it cost %f seconds'%(time_cost))
        return result

    return inner_func


class HiddenPrints:
    '''
    上下文管理器,隐藏函数输出
    '''

    def __init__(self, activated=True):
        '''
        activated参数表示当前修饰类是否被激活
        :param activated:True 隐藏函数输出
        '''
        self.activated = activated
        self.original_stdout = None

    def open(self):
        sys.stdout.close()
        sys.stdout = self.original_stdout

    def close(self):
        self.original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        # 这里的os.devnull实际上就是Linux系统中的“/dev/null”
        # /dev/null会使得发送到此目标的所有数据无效化，就像“被删除”一样
        # 这里使用/dev/null对sys.stdout输出流进行重定向

    def __enter__(self):
        if self.activated:
            # self.status()
            self.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.activated:
            self.open()

    def status(self):
        if self.activated:
            print('函数输出结果已经隐藏')
        elif not self.activated:
            print('函数输出结果正常')


if __name__ == '__main__':
    @only_time
    @catch_except
    # @show_time
    def add(a, b):
        '''

        :param a:
        :param b:
        :return:
        '''
        num = 1
        while True:
            print(num)
            # b = c
            num += 1
            if num == 1000:
                break


    print(add(2, 3))


    # print(time.time())

    def my_func():
        for i in range(1000):
            print(i)
        return True


    with HiddenPrints() as f:
        stats = my_func()
    # print(stats)
