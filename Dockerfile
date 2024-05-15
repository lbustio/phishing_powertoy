FROM python:3.9.18-slim-bullseye

WORKDIR /app/
COPY ./requirements.txt /app/
RUN apt update \
	&& apt install -y \
		cmake \
		g++ \
		gcc
RUN python -m venv .venv \
	&& . .venv/bin/activate \
	&& pip install --upgrade pip

RUN env PATH=/app/.venv/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  VIRTUL_ENV=/app/.venv LANG=C.UTF-8 CMAKE_MAKE_PROGRAM=/usr/bin/make CMAKE_C_COMPILER=/usr/bin/gcc CMAKE_CXX_COMPILER=/usr/bin/g++ pip install -r requirements.txt

COPY ./images/screenshot.png ./images/Image-Banner_1.png /app/images/
COPY  ./config.py ./utils.py ./condition_parser.py ./app.py ./vectorial_representation.py /app/
COPY ./models/all_kpe.txt ./models/rules_en.txt ./models/rules.txt /app/models/

ENV PATH=/app/.venv/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  VIRTUL_ENV=/app/.venv LANG=C.UTF-8
CMD ["env", "PATH=/app/.venv/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "streamlit", "run", "app.py"]
