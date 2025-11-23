FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 7860
ENV MLFLOW_TRACKING_URI=http://mlflow:5000 PORT=7860
CMD ["python", "app.py"]