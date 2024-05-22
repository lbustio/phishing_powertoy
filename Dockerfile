FROM python:3.9.18-slim-bullseye as builder

WORKDIR /app/
COPY ./requirements.txt /app/
RUN apt update \
&& apt install -y \
    cmake \
    g++ \
    gcc \
&& python -m venv .venv \
	&& . .venv/bin/activate \
	&& pip install --upgrade pip \
&& env PATH=/app/.venv/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin VIRTUAL_ENV=/app/.venv LANG=C.UTF-8 CMAKE_MAKE_PROGRAM=/usr/bin/make CMAKE_C_COMPILER=/usr/bin/gcc CMAKE_CXX_COMPILER=/usr/bin/g++ pip install -r requirements.txt \
&& env PATH=/app/.venv/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin VIRTUAL_ENV=/app/.venv LANG=C.UTF-8 python -c "import nltk; nltk.download('punkt')" \
&& apt purge -y cmake g++ gcc \
&& apt clean

# FROM scratch
# COPY --from=builder /app/.venv /app/
# COPY --from=builder /root/nltk_data /root/nltk_data/
# COPY --from=builder /usr/local/bin /usr/local/bin/
# COPY --from=builder /usr/local/lib /usr/local/lib/
# COPY --from=builder /lib /lib/
# COPY --from=builder /lib64 /lib64/

COPY ./images/screenshot.png ./images/Image-Banner_1.png /app/images/
COPY  ./config.py ./utils.py ./condition_parser.py ./app.py ./vectorial_representation.py /app/
COPY ./models/all_kpe.txt ./models/rules_en.txt ./models/rules.txt /app/models/

ENV PATH=/app/.venv/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin VIRTUAL_ENV=/app/.venv LANG=C.UTF-8
CMD ["streamlit", "run", "app.py"]
