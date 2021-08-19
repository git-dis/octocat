FROM python:3.9-slim

ENV PIP_NO_CACHE_DIR=false
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install -U poetry

WORKDIR /octocat

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY . .

ENTRYPOINT ["python3"]
CMD ["-m", "octocat"]