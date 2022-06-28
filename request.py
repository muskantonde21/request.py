# import requests
# import json
# URL=requests.get("https://api.merakilearn.org/courses")
# DATA=URL.json()
# num=open("new.json","w")
# num1=json.dump(DATA,num,indent=4)
# serial_no=0
# for i in range(0,len(DATA)):
#     print(serial_no+1,".",DATA[i]["name"],"ID:",DATA[i]["id"])
#     serial_no+=1
# courses_name=int(input("enter your course number which you want to learn   :"))
# print(DATA[courses_name-1]["name"])
# # print(courses_name)
# URL2=requests.get('https://api.merakilearn.org/courses/'+str(DATA[courses_name-1]["id"])+'/exercises')
# file=URL2.json()
# file1=open("data1.json","w")
# file2=json.dump(file,file1,indent=4)
# list2=[]
# data=0
# data_1=1

# for i in file["course"]["exercises"]:   
#     if i["parent_exercise_id"]==None:
#         data=data+1
#         list2.append(i)
#     if i["parent_exercise_id"]==i["id"]:
#         print(data+1,".",i["name"])
#         list2.append(i)
#         data=data+1   
#     if i["parent_exercise_id"]!=i["id"]:
#         print(" ",data_1,".",i["name"])
#         list2.append(i)
#     data_1=data_1+1
# with open("data2.json","w") as f:
#     json.dump(list2,f,indent=4)
# topic_no=int(input("choose topic number which you want to learn : "))
# for l in range(0,len(list2)):
#     if topic_no==l+1:
#         print(topic_no,list2[l]["name"])
#         a=list2[l]["parent_exercise_id"]
# var=1
# var_1=[]
# var_2=[]
# for d in range(0,len(list2)):
#     if list2[d]["parent_exercise_id"]==a:
#         print(" ",var,list2[d]["name"])
#         var_1.append(list2[d]["name"])
#         var_2.append(list2[d]["content"])
#         var+=1
# child_number=int(input("which child you want to print : "))
# # question=child_number-1
# print(var_2[child_number-1])
# question=child_number-1
# while child_number>0 :
#     next_question=input("do you next question or previous question n/p :- ")
#     if child_number==len(var_2):
#         print("next page")
#     if next_question=="p" :
#         if child_number==1:
#             print("no more questions")
#             break
#         else:
#             child_number=child_number-1
#             print(var_2[child_number])
#     if next_question=="n":
#         if child_number<len(var_2):
#             index=child_number+1
#             print(var_2[index-1])
#             question=question+1
#             child_number=child_number + 1 
#             if question==(len(var_2)-1) :
#                 print("next page")              
#                 break