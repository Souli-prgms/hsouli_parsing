ARG PYTHON_VERSION=3.11
FROM public.ecr.aws/docker/library/python:$PYTHON_VERSION as builder

ARG POETRY_VERSION=1.7.1

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
ENV MAKEFLAGS="-j 8"

SHELL ["/bin/bash", "-c"]

COPY pyproject.toml ./poetry.lock ./

RUN pip install poetry=="$POETRY_VERSION" \
  && poetry export --format requirements.txt --output requirements.txt --without-hashes --without-urls


FROM public.ecr.aws/docker/library/python:${PYTHON_VERSION}-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV MAKEFLAGS="-j 8"

WORKDIR ${JCI_BUILD_PATH}

COPY --from=builder requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "-m", "parsing_assignment", "./tests/examples/data.log"]
