FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN python3 -m venv /retirement/venv/
ENV PATH "/retirement/venv/bin:$PATH"
RUN apt-get update && \
    git clone --depth 1 --branch {{ RETIREMENT_TUBULAR_VERSION }} https://github.com/openedx/tubular.git ./tubular
WORKDIR ./tubular
COPY config.yml .
COPY run_retirement_pipeline.sh .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --exists-action w && \
    mkdir learners_to_retire
