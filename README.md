**Wymagania**
- python 3.11
- node.js v20.15
- yarn 1.22
  
**Instrukcja uruchamiania**
```
python -m venv venv
source venv/bin/activate (activating virtual environment on linux)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python -m tools.fill_db (running tool which fills database with data from api)
cd frontend
yarn install
yarn dev
```
