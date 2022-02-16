# sqlalchemy
SQLAlchemy trial from https://www.youtube.com/watch?v=uzPSOz2eNlM

1. 가상파일 생성 create virtual file
python -m venv env

2. sqlalchemy 다운 
pip install sqlalchemy

3. create requiremets.txt 
pip freeze > requirements.txt

-------------------------------------------
4.다음 코드를 python shell 에서 실행합니다. 
  run codes below in python shell

import sqlalchemy
import models 

5.데이터 생성 (create data)
sun2 = [models.Pet(name = 'sun2', age = 3, pet_type = 'human')]

6. 데이터 session에 넣기 / tying the session to the engine (sqlite:///pets.db)
models.session.add_all(sun2)

7. commit 하기
models.session.commit()

8. sqllite로 데이터 확인하기 check the table using sqlite
파이썬 shell exit 
----------------------------------------------------

D:\SQLAlchemy>sqlite3.exe pets.db
sqlite> .table 
# pets 확인
--- sql 코드로 데이터 확인하기 


fix read me file