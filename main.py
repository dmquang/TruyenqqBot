import undetected_chromedriver as uc
from time import sleep
from threading import Thread

def TruyenQQ(cookie,url_truyen):
    options = uc.ChromeOptions()
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument("--app=https://truyenqqhot.com/")
    options.add_argument("--window-size=350,550")
    driver = uc.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.execute_script('document.querySelector("#left-banner > div > span").click()')
    c = cookie.replace(" ","").split(";")
    for i in c:
        if i !="":
            ck = i.split("=")
            dict_ck = {"name":ck[0],"value":ck[1],"domain":".truyenqqhot.com"}
            driver.add_cookie(dict_ck)
    driver.refresh()
    driver.get(url_truyen)
    driver.execute_script('document.querySelector("body > div.content > div.div_middle > div.main_content > div > div.book_info > div.book_other > ul.story-detail-menu > li.li01 > a").click()')
    driver.minimize_window()
    while True:
        try:
            for i in range(1500):
                driver.execute_script(f'scroll(0,{i*3})')
            try:
                driver.execute_script('document.querySelector("#chapter_content > div > div.chapter_content > div.chapter_control > a.next.control-button.link-next-chap").click()')
                pass
            except:
                print(f'Done: {url_truyen.split("truyen-tranh/")[1]}')
                driver.quit()
                break
                quit()
        except:
            print('loi j roi')
            sleep(10)
            driver.quit()
            quit()

if __name__ == '__main__':
    cookie = '' #cookie truyenqq
    list_truyen = ['rul truyen']
    a = 0
    for i in list_truyen:
        url_truyen = i.split('\n')[0]
        t = Thread(target=TruyenQQ,args=(cookie, url_truyen))
        t.start()
        a+=1
        if a == 3:
            sleep(180)
            a = 0
