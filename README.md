**Wymagania**
- python 3.11
- node.js v20.15
- yarn 1.22
  
**Instrukcja uruchamiania**
```
python -m venv venv
source venv/bin/activate (instrukcja uruchomienia środowiska wirtualnego pythona na linuxa)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

cd frontend
yarn install
yarn dev
```
