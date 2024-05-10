FROM python:3.9.18-alpine

COPY ./config.py ./utils.py ./requirements.txt ./Pipfile ./Procfile ./condition_parser.py ./app.py ./vectorial_representation.py /app/
COPY ./images/screenshot.png ./images/Image-Banner_1.png /app/images/
COPY ./files/all_kpe.txt ./files/rules_en.txt ./files/rules.txt /app/files/

WORKDIR /app/

RUN apk update \
    && apk add --no-cache gcc g++ \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk del gcc g++;

#CMD ["streamlit", "run", "phishing_detector.py"]
CMD ["sh", "-c", "while true; do sleep 1000; done"]
