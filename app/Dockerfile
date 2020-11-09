FROM python:3.7

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY __init__.py /app
CMD ["python","-u","__init__.py"]
