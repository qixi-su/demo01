#   是另一种可变容器模型，且可存储任意类型对象。字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中。
#   fornkeys
#   用于创建包含指定key的字典，如果不指定默认值则为None
# 不指定默认值
re = dict.fromkeys(['a','b','c'])
print(re)
# 指定默认值
ra = dict.fromkeys(["a","b","c"],1)
print(ra)