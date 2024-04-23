FROM python

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir nltk
CMD ["python" , "app.py"]