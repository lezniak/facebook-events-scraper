import re
import requests
import os


counter=0
with open('links.txt', 'r') as f:
  for line in f:
    temp = open('links.txt','r').read().split('\n')
    headers = {'User-agents':'Mozilla/5.0'}
    html_data = requests.get(temp[counter],headers=headers)
    html_data = html_data.text
    counter += 1
    file = open('fbSource.txt','wb') 
    file.write(html_data.encode('UTF-8'))
    file.close()
    if True == True:
        file = open('fbSource.txt','r',encoding='utf-8')  
        for x in range(10000):
            lock = False   
            char = file.read(1)   
            if char == 'a':
                if file.read(1) == 'd':       
                    if file.read(1) == 'd': 
                        if file.read(1) == 'r': 
                            if file.read(1) == 'e':
                                if file.read(1) == 's':
                                    if file.read(1) == 's':
                                        file.read(2)
                                        loc=""
                                        while not (x == '}'):
                                            lock = True
                                            x = file.read(1)
                                            loc = loc + x
                                    break   
        file.close()  
        if lock == False:
            print("[%s]Error code #1"%counter)
        else:                     
            loc = re.sub(r"[-()#/@;:<>{}`+=~|!?,]", "", loc)
            x = loc.split("\"")
            dane = [x[11],x[19]]
            file = open('fbSource.txt', 'r') 
            for x in range(10000): 
                char = file.read(1)   
                if char == 's':
                    if file.read(1) == 't':
                        if file.read(1) == 'a': 
                            if file.read(1) == 'r': 
                                if file.read(1) =='t':
                                    if file.read(1) == 'D':
                                        file.read(5)
                                        date=""
                                        for i in range (26):
                                            x = file.read(1)
                                            date = date + x
                                        break
            file.close()
            date = re.sub(r"\"", "", date)
            x = date.split("T")
            dane.append(x[0])
            b = x[1]
            b = b.split("+")
            dane.append(b[0])

            file = open('fbSource.txt', 'r',encoding='utf-8') 
            for x in range(10000): 
                char = file.read(1)   
                if char == ',':
                    if file.read(1) == '\"':
                        if file.read(1) == 'n': 
                            if file.read(1) == 'a': 
                                if file.read(1) =='m':
                                    if file.read(1) == 'e':
                                        file.read(3)
                                        name=""
                                        x=''
                                        while not (x == '\"'):
                                            name = name + x
                                            x = file.read(1)
                                        break
            dane.append(name)
            with open("result.txt", "a") as file:
                file.write(str(dane)+"\n")
                print ("[%s]Success!"%counter)
                os.remove("fbSource.txt")