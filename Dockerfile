#use offical python 3.11 slim # 3.11 is version and slim is a lightweight storage images
FROM python:3.11-slim

# set work dictory    #### this app is folder that docker will create and copy all the files
WORKDIR /app

#copy  requirements file
COPY requirements.txt .
COPY wine_model.joblib .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy all files in container
COPY . .

# Expose port FastAPI will run on
EXPOSE 8000

#command to run FastAPI with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]