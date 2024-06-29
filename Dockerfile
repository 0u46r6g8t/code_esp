FROM python:3.10.12 as base

# [1] - Configuration virtualenv
RUN pip install virtualenv

RUN python -m venv env

RUN /bin/bash -c "source /env/bin/activate"

# [2] - Create application
WORKDIR /app

COPY ./container/requirements.txt /app/requirements.txt 

COPY ./src /app/

# [3] - Installation of requirements
# RUN apt-get install -y cmake

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Installing dependencies

RUN apt update -y

RUN pip install uvicorn[standard] fastapi

COPY . .

# [5] - Running the application
CMD ["python", "-m", "uvicorn", "src.__main__:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]