#!/bin/bash

# Build all Docker images
echo "Building Docker images..."
docker compose build

# Run the tests
echo "Running tests..."
docker compose up --abort-on-container-exit

# Check if the log file exists before trying to extract it
echo "Checking if log file exists in volume..."
if docker run --rm -v log-volume:/log alpine ls /log/api_test.log 2>/dev/null; then
    # Extract logs
    echo "Extracting logs..."
    docker run --rm -v log-volume:/log alpine cat /log/api_test.log > log.txt
    echo "Logs extracted to log.txt"
else
    echo "Error: No log file found in volume. Checking container outputs..."
    # Get logs from each test container to debug
    docker compose logs auth_test > auth_test_logs.txt
    docker compose logs authorization_test > authorization_test_logs.txt
    docker compose logs content_test > content_test_logs.txt
    echo "Container logs saved to auth_test_logs.txt, authorization_test_logs.txt, content_test_logs.txt"
fi

# Clean up
echo "Cleaning up..."
docker compose down
docker volume rm -f log-volume

echo "Process completed. Check the log files for details."

#=================Terminal==============
#Before running setup.sh, you can check inside the container whether the log is really written:
    #docker compose run --rm auth_test sh -c "cat /log/api_test.log"
#Excution and Results to be done on my Terminal
#make the setup.sh script executable
#chmod +x setup.sh
#Run the tests: ./setup.sh
#=================Terminal==============