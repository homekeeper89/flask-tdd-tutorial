#  application/run.py
# 만들어진 서버 객체를 실행한다.

from create import create_app

app = create_app()

if __name__ == '__main__':
    app.run()