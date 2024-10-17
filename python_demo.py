# 实现一个wordcount函数，统计英文字符串中每个单词出现的次数。返回一个字典，key为单词，value为对应单词出现的次数。
# ---------input----------
#"""Hello world!  
# This is an example.  
# Word count is fun.  
# Is it fun to count words?  
# Yes, it is fun!"""

# ----------output----------
# {'hello': 1, 'world': 1, 'this': 1, 'is': 4, 'an': 1, 'example': 1, 'word': 1, 'count': 2, 'fun': 3, 'it': 2, 'to': 1, 'words': 1, 'yes': 1}




# 方法一：
'''
def wordcount(text):
    # 处理替换标点符号，转为小写
    punction  = ".,!?;;'\"()"
    for p in punction:
        text = text.replace(p, "")
    text = text.lower()
    
    word_list = text.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] =1
    
    print(word_dict)
        
wordcount(text)

'''

import re
from collections import Counter
def word_count(text):
    # 处理替换标点符号，转为小写
    words = re.findall(r'\b\w+\b', text.lower())
    
    return dict(Counter(words))

text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

word_count_result = word_count(text)
print(word_count_result)