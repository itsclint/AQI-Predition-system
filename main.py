# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




FROM ubuntu:latest

# Install required packages
RUN apt-get update
RUN apt-get install dos2unix
RUN apt-get install bash
RUN apt-get install cron

# Install python/pip
RUN apt-get install -y python3-pip
ENV PYTHONUNBUFFERED=1
# install Python requirements
RUN pip3 install colorama requests python_dotenv python_dateutil
RUN pip3 install numpy
RUN pip3 install pandas

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