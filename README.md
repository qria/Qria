#1. 개발 시작

pycharm에서 new Flask project

virtualenv 에서 새로운 virtual environment인 pyBoard생성

pyBoard.py 실행하고 127.0.0.1:5000 에 Helllo World 뜨는것 확인

git 생성하고 pyBoard.py, README.md 를 git에 추가 후 커밋

git remote add origin https://github.com/qria/pyBoard.git

git push -u origin master

#2. index.html 추가

'/'와 '/index'에 라우팅

app.run에 debug=True 파라미터 추가. 이제 코드바뀌면 서버 자동 재시작

#3. templates 생성

base, 그리고 거기 들어갈 header, navbar, footer, script 생성

참고로 base.html 제외하고는 모두 빈 파일

index는 base의 content block을 상속해서 재작성