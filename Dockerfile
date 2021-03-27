FROM python:3.7.9
COPY  . /api
WORKDIR /api
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]