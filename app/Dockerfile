FROM python:3.9-alpine AS builder

WORKDIR /opt/app

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml ./
RUN pip install poetry==1.1.12

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi


FROM  python:3.9-alpine AS production

# COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /opt/app/.venv /opt/app/.venv

ENV PATH="/opt/app/.venv/bin:$PATH"



WORKDIR /opt/app

COPY api ./api 
COPY main.py .
COPY config.py . 

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--log-level", "debug", "main:app"]