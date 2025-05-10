FROM python:alpine AS builder
WORKDIR /app

RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    /bin/uv sync --locked --no-install-project --no-editable --no-dev

FROM python:alpine AS runner

WORKDIR /app

COPY --from=builder --chown=app:app /app/.venv .venv/

COPY . .
RUN rm -f pyproject.toml uv.lock && chmod u+x .venv/bin/activate
