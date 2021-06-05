import os
import filename

# print(filename.real_name)

path = 'D:/Downloads/ESL'
file_names = os.listdir(path)
print(file_names)

i = 0
for name in file_names:
    old_name = path +'/'+ file_names[i] #读取单个文件现有名字
    new_name = path + '/' + filename.real_name[i] + '.mp3'
    # newname = new_name[:-4] + '.pdf' #替换文件扩展名
    os.rename(old_name,new_name)  #重命名
    i += 1
