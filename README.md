1. 아래 경로에서 크롬, 크롬드리이버 다운로드
> https://googlechromelabs.github.io/chrome-for-testing/

2. 최초 설치시
```
python3 -m venv pythonCarwler
cd pythonCarwler
source venv/bin/activate
pip3 install selenium
pip freeze > requirements.txt
```

3. 그 이후 재실행시
```
python3 -m venv pythonCarwler
cd pythonCarwler
source venv/bin/activate
pip install -r requirements.txt
```