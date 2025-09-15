FROM python:3.12-alpine
WORKDIR /app
RUN apk upgrade --no-cache  
# RUN apt-get update

# / => root , ~ => home , . => current directory , ..=> go to the parent directory

# . => it means current directory , /app
# .. => it means parent directory , /
# ./app => it means /app/app


COPY requirements.txt . 
RUN pip install -r  requirements.txt
COPY . .

EXPOSE 8000
# CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
CMD ["sh","-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]