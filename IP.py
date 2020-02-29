# n=int(input('enter an integer >=0: '))
# fact=1
# for i in range(2,n+1):
#     fact=fact * i
# print(str(n) + ' factorial is ' + str(fact))

#随机产生IP地址，并且打印到屏幕上
import random
section1 = random.randint(1,254)
section2 = random.randint(1,254)
section3 = random.randint(1,254)
section4 = random.randint(1,254)
random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
print('随机产生的IP地址: ' + random_ip)