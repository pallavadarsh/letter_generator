FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --prefer-binary --force-reinstall blis
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0.tar.gz

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
