try:
    file = open("newfile","r+") # r+表示read加写入
except Exception as e:
    print("there is no file named eeee")
    response = input("do you want to create a new file")
    if response == "y":
        file = open("newfile","w")
    else:
        pass
else:
    file.write("hello world") # 如果存在newfile这个文件，则写入hello world
file.close()