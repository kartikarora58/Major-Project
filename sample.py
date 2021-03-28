import os
import shutil
f=open('classes.txt','r')

temp=[]
for x in f:
    temp.append(x.strip())

qw=[]
classes=[]
for item in temp:
    qw=[]
    for char in item.split():
        try:
            int(char)

        except:
            qw.append(char)

    classes.append(qw)
final_list=[]

for item in classes:
    final_list.append(" ".join(item))
print(final_list)

with open('class.txt','a') as output:
    for item in final_list:
        output.write(item)
        output.write('\n')

# image_name=[]
# label=[]
# a=open('val.txt','r')

# image_data={}
# for item in a:
#     image_data[list(item.split())[0]]=int(list(item.split())[1])
# # print(image_data)
# # for item in final_list:
# #     parent_dir='E:/Major Project/dataset/ip102_v1.1/validation'
# #     path=os.path.join(parent_dir,item)
# #     os.mkdir(path)

# for item in image_data.items():
#     print(item)
#     shutil.move(f'E:/Major Project/dataset/ip102_v1.1/images/{item[0]}',f'E:/Major Project/dataset/ip102_v1.1/validation/{final_list[item[1]]}')





    
