# using official python image 
FROM python:3.11


# defining the working directory in the container
WORKDIR /CC

# Copying requirements.txt at CC inside the container 
COPY requirements.txt /CC/

# Installing the dependencies without cache
RUN pip install --no-cache-dir -r requirements.txt

# Copying the rest of the files from host working directory to the container directory 
COPY . /CC

# Exposing the port
EXPOSE 8501

# Running commands
CMD ["streamlit", "run", "app.py"] 