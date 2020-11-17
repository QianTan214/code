"""设计一个函数返回给定文件名的后缀名"""

def get_suffix(filename):
    index = filename.rfind(".") # 虽然是rfind，index也是从左往右数
    # print(index)
    return filename[index + 1:] if index > 0 else ""


print(get_suffix("readme.txt")) # txt
print(get_suffix("readme.txt.md")) # md
print(get_suffix('.readme')) #
print(get_suffix('readme.')) #
print(get_suffix('readme'))  #