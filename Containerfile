FROM python:3.10

# working directory
WORKDIR /app

# copy requirements
COPY requirements.txt .

# install python packages
RUN pip install -r requirements.txt

# copy application files
COPY app/ /app

# expose port
EXPOSE 5000

# run the app
CMD ["python", "app.py"]
