FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN python3 -m venv /retirement/venv/
ENV PATH "/retirement/venv/bin:$PATH"
RUN apt-get update && \
    git clone --depth 1 --branch {{ OPENEDX_COMMON_VERSION }} https://github.com/openedx/edx-platform.git 
WORKDIR ./edx-platform
COPY run_retirement_pipeline.sh scripts/user_retirement/
RUN pip install --upgrade pip && \
    pip install -r scripts/user_retirement/requirements/base.txt --exists-action w && \
    mkdir scripts/user_retirement/learners_to_retire
