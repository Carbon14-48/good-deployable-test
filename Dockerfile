FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 8000
CMD ["python", "app.py"]
