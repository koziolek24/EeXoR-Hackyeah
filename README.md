instrukcja uruchamiania

python -m venv venv (my korzystaliśmy z python 11)
source venv/bin/activate (instrukcja uruchomienia środowiska wirtualnego pythona na linuxa)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

cd frontend
yarn install
yarn dev

