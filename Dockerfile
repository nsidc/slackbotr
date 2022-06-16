FROM mambaorg/micromamba:0.23.3

WORKDIR /opt/slackbotr

# Activate the conda environment during build process
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# NOTE: For some reason, micromamba doesn't like the filename
# "environment-lock.yml". It fails to parse it because it's missing some
# special lockfile key.
COPY environment-lock.yml ./environment.yml

# Install dependencies to conda environment
RUN micromamba install -y \
    # NOTE: -p is important to install to the "base" env
    -p /opt/conda \
    -f environment.yml
RUN micromamba clean --all --yes


COPY ./.flake8 ./
COPY ./.mypy.ini ./
# NOTE: Directories can't be copied to `.` or only contents will be copied, so
# we need one line per dir:
COPY ./seaiceservice ./seaiceservice
COPY ./scripts ./scripts
COPY ./tasks ./tasks

# Test conda environment is correctly activated
RUN python -c "import fastapi"
RUN which gunicorn

EXPOSE 5000

#  https://www.uvicorn.org/deployment/#using-a-process-manager
CMD ["gunicorn", "slackbotr.api:api", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5000", "--log-level", "debug"]
