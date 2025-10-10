
## python
FROM python:3.11-slim

## app is name given for working dir
WORKDIR /app

COPY requirements.txt .

## --no-cache-dir is to stop creation of unnecessary file 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

