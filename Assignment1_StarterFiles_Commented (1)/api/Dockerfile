FROM python:3.12-slim  # base image
WORKDIR /app  # working dir
COPY requirements.txt .  # copy deps
RUN pip install -r requirements.txt  # install deps
COPY app.py .  # copy app code
EXPOSE 5000  # expose port
CMD ["python","app.py"]  # run app
