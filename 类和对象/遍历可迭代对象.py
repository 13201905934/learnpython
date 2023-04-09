# 处理系统产生的异常
import sys

word = 'you say you always love me'
words = iter(word)
while True:
    try:
        print(next(words))
    except:
        sys.exit()
