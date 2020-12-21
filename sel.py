from selenium import webdriver
import pyautogui
import pyperclip
# pyautogui.PAUSE = 3

url = "https://www.youtube.com/playlist?list=PLdEdazAwz5Q_n47tqf0QY94ASCmWqeGX1"
browser = webdriver.Chrome() 
browser.get(url)

# with open("ytb_list.html","w",encoding="utf-8") as f:
#     f.write(browser.page_source)

elements = browser.find_elements_by_class_name('yt-simple-endpoint')
lst =[]

for idx, element in enumerate(elements):
    if "https://www.youtube.com/watch?" in str(element.get_attribute("href")):
        if idx % 2 == 0:
            lst.append(element.get_attribute("href"))
print(lst)
print(len(lst))


w = pyautogui.getWindowsWithTitle("4K Video Downloader – 비활성화")[0]

# print(w)
if w.isActive == False:
    w.activate()

for url in lst:
    pyperclip.copy(str(url))
    pyautogui.click(w.left+40,w.top+100,duration= 1)
    pyautogui.click(w.left+480,w.top+480,duration= 1)