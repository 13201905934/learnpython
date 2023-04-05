import re

thing = 'your dog is your all best friend'
hu = re.match('ou', thing)
print(hu)  # None

hu1 = re.match('your', thing)
print(hu1)
print(hu1.group())  # your
print(hu1.span())  # (0, 4)
print(hu1.string)  # your dog is your all best friend
