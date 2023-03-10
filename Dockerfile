# Start with an Alpine 3.15 base image
FROM alpine:3.15

# Install required packages
RUN apk add --update --no-cache bash dos2unix

# Install Python 3 and create symlink to use it as default
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

# Install dependencies required for numpy and pandas
RUN apk add build-base python3-dev openblas-dev lapack-dev

# Set environment variable to ensure Python output is unbuffered
ENV PYTHONUNBUFFERED=1

# Install Python packages using pip
RUN python3 -m ensurepip --upgrade
RUN pip3 install colorama requests python_dotenv
RUN /usr/bin/python3 -m pip install --upgrade pip
RUN pip3 install numpy
RUN pip3 install Pandas

# Set working directory for the container
WORKDIR /usr/scheduler

# Copy the necessary files into the container
COPY jobs/*.* ./jobs/
COPY crontab.* ./
COPY start.sh .

# Convert line endings and make scripts executable
RUN dos2unix crontab.* *.sh jobs/*.* \
    && \
    find . -type f -iname "*.sh" -exec chmod +x {} \; \
    && \
    find . -type f -iname "*.py" -exec chmod +x {} \;

# Create log file for cron
RUN touch /var/log/cron.log

# Start cron when the container starts up
CMD ["./start.sh"]
