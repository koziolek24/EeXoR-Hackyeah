FROM python:3.12 AS base

WORKDIR /src
RUN python3 -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY __init__.py  manage.py ./
COPY EeXoR/ ./EeXoR
COPY main_system/ ./main_system

FROM base AS db_builder
COPY tools ./tools
RUN python3 manage.py migrate
RUN python3 -m tools.fill_db

FROM base
COPY --from=db_builder /src/db.sqlite3 ./
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000