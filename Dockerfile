FROM python:3.9.18-alpine

WORKDIR /app/
COPY ./requirements.txt /app/
RUN apk update \
	&& apk add --no-cache \
		cmake \
		g++ \
		gcc
RUN python -m venv .venv \
	&& . .venv/bin/activate \
	&& pip install --upgrade pip \
	&& pip install -r requirements.txt

COPY  ./config.py ./utils.py  ./Pipfile ./Procfile ./condition_parser.py ./app.py ./vectorial_representation.py /app/
COPY ./images/screenshot.png ./images/Image-Banner_1.png /app/images/
COPY ./files/all_kpe.txt ./files/rules_en.txt ./files/rules.txt /app/files/

#CMD ["streamlit", "run", "phishing_detector.py"]
CMD ["sh", "-c", "while true; do sleep 1000; done"]
