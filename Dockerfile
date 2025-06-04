FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/usr/src/app
