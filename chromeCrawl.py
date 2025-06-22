from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import urllib

# 셋팅
chrome_binary_path = "chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
chromedriver_path = "chromedriver-mac-arm64/chromedriver"
options = Options()
options.binary_location = chrome_binary_path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def startCrawling(gender, face_type, person):
    driver.get("https://www.google.com/imghp?hl=ko&ogbl")
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(str(person))
    elem.send_keys(Keys.RETURN)
    time.sleep(2)

    number = 1
    images = driver.find_elements(By.CSS_SELECTOR, ".mNsIhb")
    save_dir = f"output/{gender}/{face_type}/{person}"
    os.makedirs(save_dir, exist_ok=True)

    for image in images:
        if number > 50:
            break

        try:
            image.click()
            time.sleep(2)
            img_url = driver.find_elements(By.CSS_SELECTOR, ".sFlh5c.FyHeAf.iPVvYb")[0].get_attribute("src")
            file_ext = os.path.splitext(urllib.parse.urlparse(img_url).path)[1]
            file_name = f"{number}{file_ext}"
            save_path = os.path.join(save_dir, file_name)

            urllib.request.urlretrieve(img_url, save_path)
        except:
            pass

        number = number+1


persons = {
    "여자": {
        "고양이상": ["김소현", "한예슬", "아이유", "김지원", "전지현"],
        "토끼상": ["정은지 (에이핑크)", "박보영", "오마이걸 아린", "임윤아 (소녀시대)", "트와이스 나연"],
        "여우상": ["선미", "서현진", "정려원", "레드벨벳 아이린", "한소희"],
        "사슴상": ["수지", "박지현", "고윤정", "이성경", "정수정 (크리스탈)"],
        "강아지상": ["김세정", "혜리 (걸스데이)", "트와이스 사나", "아이브 장원영", "박신혜"],
        "햄스터상": ["레드벨벳 웬디", "트와이스 쯔위", "(여자)아이들 우기", "에이프릴 나은", "러블리즈 케이"]
    },
    "남자": {
        "공룡상": ["김우빈", "이민호", "안보현", "류준열", "박서준"],
        "곰상": ["마동석", "조세호", "유재석", "박보검", "차태현"],
        "강아지상": ["박지훈", "뷔 (BTS)", "이승기", "육성재", "강다니엘"],
        "고양이상": ["서강준", "이준기", "차은우", "김재중", "이도현"],
        "토끼상": ["도영 (NCT)", "정국 (BTS)", "장기용", "이찬혁 (악뮤)", "여진구"],
        "햄스터상": ["엑소 시우민", "비투비 정일훈", "샤이니 태민", "세븐틴 승관", "NCT 해찬"]
    }
}

for gender, types in persons.items():
    for face_type, names in types.items():
        for name in names:
            try:
                print(f"[INFO] 크롤링 시작: {gender} / {face_type} / {name}")
                startCrawling(gender, face_type, name)
                print(f"[INFO] 완료: {gender} / {face_type} / {name}")
            except Exception as e:
                print(f"[ERROR] 실패: {gender} / {face_type} / {name} → {e}")
