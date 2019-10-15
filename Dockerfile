# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
COPY . /multiple_thread_automation_test
WORKDIR  /multiple_thread_automation_test
# set maintainer
LABEL maintainer "kaige8531917@163.com"
# Copy the current directory contents into the container at /app
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
#VOLUME [ "/multiple_thread_automation_test/sunnytest" ]
# Run app.py when the container launches
CMD pytest --html=multiple_thread_automation_test/sunnytest/reportbytester.html
#COPY . /multiple_thread_automation_test/sunnytest