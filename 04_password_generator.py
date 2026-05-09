import random
import string
# 拿用户输入，转 int
length = int(input("password_length: "))                                
# 备好字符库
chars = string.ascii_letters + string.digits + string.punctuation  
# 抽 length 个 + 拼成字符串
password = ''.join(random.choices(chars, k=length))               
print(f"your_password_is: {password}")                                  