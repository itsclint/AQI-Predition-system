#!/bin/bash

# Check if the environment variable is set, otherwise set it to "Development"
if [ -z "$SCHEDULER_ENVIRONMENT" ]; then
   echo "SCHEDULER_ENVIRONMENT not set, assuming Development"
   SCHEDULER_ENVIRONMENT="Development"
fi

# Select the crontab file based on the environment
CRON_FILE="crontab.$SCHEDULER_ENVIRONMENT"

echo "Loading crontab file: $CRON_FILE"

# Remove commented-out lines from the crontab file
grep -v '^#' $CRON_FILE

# Load the crontab file
crontab $CRON_FILE

echo "Starting cron..."

# Start cron in the foreground
crond -f
