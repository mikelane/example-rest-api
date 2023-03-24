FROM python:3.11

ARG APP_PATH=/api
ARG PYTHON_VERSION=3.11
ARG POETRY_VERSION=1.4.1
ARG POETRY_HOME="/opt/poetry"

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME=${POETRY_HOME}

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN pip install --trusted-host pypi.python.org -U pip setuptools wheel poetry==$POETRY_VERSION

WORKDIR $APP_PATH
COPY pyproject.toml poetry.lock $APP_PATH/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . .

EXPOSE 80

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]