Name='Elven'
Age=26

#判断数据类型
print(type(Name))
print(type(Age))

print(Name,Age)
#打印变量的内存地址
print(id(Name))
print(id(Age))
#理解变量的赋值变化
Name='Zhang'
Age=25
print(Name,Age) 
print(id(Name))
print(id(Age))
#理解字符串的索引
print(Name[4])
#理解字符串的切片
print(Name[2:4])
#字符串操作函数
#改变为全部大写
print(Name.upper())
#改变为50长度的字符串，居中，用-填写空白
print(Name.center(50,'-'))

#多行字符串,在字符串里面引用外部变量
Name='''
%s Zhangyx
IS
Big
King
Age is %s
'''%(Name,Age)
print(Name)

# %s str %d digit %f float

#直接在字符串里面引用外部变量
Name=f'''
{Name} Zhangyx
IS
Big
King
Age is {Age}
'''

print(Name)
#字符串类型转换
print (Name+str(Age))

#占位符引用外部变量
Name='''
Zhangyx
IS
Big
King
'''


#删除变量
del Name