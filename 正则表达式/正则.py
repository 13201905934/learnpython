import re

thing = 'your dog is your all best friend'
hu = re.search('^your.*friend$', thing)
if hu:
    print('yes! you have best friend')
else:
    print('sorry! you have no best friend!')

# 输出d-n的字符
hu1 = re.findall('[d-n]', thing)
print(hu1)

# 找出字符中的数字
thing1 = 'this is a 250 dog'
hu2 = re.findall('\d', thing1)
print(hu2)  # ['2', '5', '0']

# 找出your
hu3 = re.findall('yo..', thing)
print(hu3)  # ['your', 'your']
# 找出以y开头,后面跟两个字母
hu4 = re.findall('^y..', thing)
print(hu4)  # ['you']

# 以f开头以d结尾，中间出现一次或多次字母
hu5 = re.findall('f.*d$', thing)
print(hu5)  # ['friend']

# thing中包含y或d，其后跟0个或多个0
hu6 = re.findall('[y|d]o*', thing)
print(hu6)  # ['yo', 'do', 'yo', 'd']

# thing中包含y或d，其后跟1个或多个0
hu7 = re.findall('[y|d]o+', thing)
print(hu7)  # ['yo', 'do', 'yo']

# thing中包含a其后必须跟两个字符l的字符串
hu8 = re.findall('al{2}', thing)
print(hu8)  # ['all']

# 对thing进行以空白格进行分隔
hu9 = re.split('\s', thing)
print(hu9)

# 对thing分割 在空白格第一次出现和第二次出现时分割字符
hu9 = re.split('\s', thing, 2)
print(hu9)  # ['your', 'dog', 'is your all best friend']

# 替代函数sub 对空格用;替代
hu10 = re.sub('\s', ';', thing)
print(hu10)  # your;dog;is;your;all;best;friend

# 对前两个用;替代
hu11 = re.sub('\s', ';', thing, 2)  # your;dog;is your all best friend
print(hu11)
