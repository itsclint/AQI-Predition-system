
# AQI Jobs Scheduler

This project is a simple scheduler for fetching air pollution data using OpenWeatherMap API. It includes a Dockerfile for building a Docker image and a crontab file for scheduling the data fetching job.


## Getting Started

### Prerequisites
Before running this project, you need to have Docker installed on your machine.

Docker: https://www.docker.com/get-started

### Installation
Clone this repository:

## Installation

1. Clone this repository:

```bash
git clone https://github.com/itsclint/AQI-jobs-scheduler.git

```
2. Navigate to the project directory:

```bash
cd AQI-jobs-scheduler

```
3. Create a .env file in the project directory and add your OpenWeatherMap API key as follows:
```bash
API_KEY=your_api_key_here
```
4. Build the Docker image:
```bash
docker build -t aqi-jobs-scheduler .

```

## Usage
To start the scheduler, run the following command:
```bash
docker run --rm --name aqi-jobs-scheduler -d aqi-jobs-scheduler
```

This will start a Docker container with the scheduler running in the background. The scheduler will fetch air pollution data every minute and save it to a CSV file in the data directory.

To stop the scheduler, run the following command:
```bash
docker stop aqi-jobs-scheduler
```


## Authors

- [Hauwa Umar](https://github.com/HauwaUmar)
- [Clinton Mbataku](https://github.com/itsclint)


## License

[MIT](https://choosealicense.com/licenses/mit/)

