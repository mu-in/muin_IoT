import requests
import webbrowser
import time
import os

import dummy

# ADMIN_KEY = ''

server = "https://mu-in.herokuapp.com/payment"
kakao = "https://kapi.kakao.com/v1/payment/ready"

def postServer(data,total):
    products = data
    for i in range(len(products)):
        del products[i]['price']
        del products[i]['category']
    
    param = {
        'storeUuid': 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaaaaaa',
        'stocks': products,
        'totalPrice': total,
    }
    
    res = requests.post(server, headers={'Content-type':'application/json'}, params=param)
    
    print(res.json())

def payment(data,quantity,total):
    header = {
        'Authorization':f'KakaoAK {ADMIN_KEY}',
        'Content-type':'application/x-www-form-urlencoded;charset=utf-8'
    }

    param = {
        'cid':'TC0ONETIME',
        'partner_order_id':'-',
        'partner_user_id':'-',
        'item_name':'뮤인 무인매장',
        'quantity':quantity,
        'total_amount':total,
        'tax_free_amount':0,
        'approval_url':'http://127.0.0.1:5000',
        'cancel_url':'http://127.0.0.1:5000',
        'fail_url':'http://127.0.0.1:5000'
    }

    res = requests.post(kakao, headers=header, params=param)
    redirect = res.json()

    webbrowser.open(url=redirect['next_redirect_pc_url'])
    
    time.sleep(10) # 10초 기다리고 닫기
    os.system("killall -9 'Safari'") # mac에서만 작동함

    postServer(data,total)

    return redirect['next_redirect_pc_url']

if __name__== '__main__':
    redirect = payment(dummy.data,1,100)
    print(redirect)