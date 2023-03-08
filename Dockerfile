FROM alpine:3.15

# Install required packages
RUN apk add --update --no-cache bash dos2unix

# Install python/pip
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add build-base python3-dev openblas-dev lapack-dev
RUN python3 -m ensurepip --upgrade
ENV PYTHONUNBUFFERED=1
# install Python requirements
RUN pip3 install colorama requests
RUN pip3 install python_dotenv

#RUN apk add python3 py3-pip
RUN /usr/bin/python3 -m pip install --upgrade pip
RUN pip3 install numpy
RUN pip3 install Pandas



WORKDIR /usr/scheduler

# Copy files
COPY jobs/*.* ./jobs/
COPY crontab.* ./
COPY start.sh .

# Fix line endings && execute permissions
RUN dos2unix crontab.* *.sh jobs/*.* \
    && \
    find . -type f -iname "*.sh" -exec chmod +x {} \; \
    && \
    find . -type f -iname "*.py" -exec chmod +x {} \;

# create cron.log file
RUN touch /var/log/cron.log

# Run cron on container startup
CMD ["./start.sh"]