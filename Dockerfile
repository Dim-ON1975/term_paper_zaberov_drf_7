# Базовый образ Python
FROM python:3.11-slim as base
LABEL maintainer="Dmitriy <zaberov.dv@internet.ru>"

# Сборка зависимостей
ARG BUILD_DEPS="curl"
RUN apt-get update && apt-get install -y $BUILD_DEPS

# Установка poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.2 POETRY_HOME=/root/poetry python3 -
ENV PATH /root/.local/bin:$PATH

# Инициализация проекта
WORKDIR /code

# Устанавливаем переменные среды для контейнера
ENV POETRY_VERSION=1.8.2 \
    PATH="$PATH:/root/poetry/bin" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Установка библиотек poetry
# --no-interaction (-n): не задавать никаких интерактивных вопросов
# --no-ansi: отключить вывод ANSI
COPY poetry.lock pyproject.toml /
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Копирование в контейнер папок и файлов
COPY . .
