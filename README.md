# Movies ETL Project Using Docker

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [How to Use](#how-to-use)
   - [Set Up the Docker Environment](#set-up-the-docker-environment)
   - [Run the ETL Process](#run-the-etl-process)
   - [Stopping and Removing the Container](#stopping-and-removing-the-container)
4. [Requirements](#requirements)
5. [Project Files](#project-files)
6. [Docker Commands](#docker-commands)
7. [Credits](#credits)

## Overview

The **Movies ETL Project** is a Python-based ETL (Extract, Transform, Load) pipeline designed to process movie rating data. The project leverages Docker to containerize the environment, ensuring the ETL process can run consistently across different setups, regardless of system dependencies.

## Features

- **Extract**: Retrieve movie ratings and movie details from local files.
- **Transform**: Clean and process the data into structured DataFrames using Python.
- **Load**: Export the cleaned and processed data into CSV files.
- **Dockerized**: The entire ETL process operates within a Docker container to guarantee a consistent environment on any platform.

## How to Use

### Set Up the Docker Environment
   - Ensure that Docker is installed and running on your machine.
   - Build the Docker image by running the following command:
     ```bash
     docker build -t movies_etl .
     ```

### Run the ETL Process
   - Execute the Docker container and mount your local folder to store the results:
     ```bash
     docker run -v /path/to/your/local/folder:/results movies_etl
     ```
   - Replace `/path/to/your/local/folder` with the path to the folder on your local machine where you want to store the output files.
   - The cleaned data will be saved as `ratings.csv` and `movies.csv` inside the specified `/results` folder.

### Stopping and Removing the Container
   - To stop the running container, press `CTRL + C` or use the following command:
     ```bash
     docker stop <container_name>
     ```
   - Once the container is stopped, remove it by executing:
     ```bash
     docker rm <container_name>
     ```

## Requirements

- **Python 3.9** (included in the Docker container)
- **Python Libraries**: pandas
  - These dependencies are automatically installed in the Docker container via the `requirements.txt` file.

## Project Files

- **`helper.py`**: Contains the `local_storage` class responsible for loading and processing the movie ratings and details.
- **`movies_etl.py`**: The main ETL script that performs the extract, transform, and load operations.
- **`Dockerfile`**: Specifies the Docker container environment and outlines the steps to run the ETL script.
- **`requirements.txt`**: Lists the required Python dependencies for the project.

## Docker Commands

- **Build the Docker Image**:
  ```bash
  docker build -t movies_etl .
  ```

- **Run the Docker Container**:
  ```bash
  docker run --name ETL_Movies -v /path/to/local/folder:/results movies_etl
  ```

Replace `/path/to/local/folder` with the desired directory on your local machine where the output files will be saved.

## Credits

- The Docker setup for this project is based on the official Docker [documentation](https://docs.docker.com/get-started/), which provides comprehensive guidelines for building and running Docker containers.
- The Python `pandas` library is used for data processing and transformation, and its documentation can be found [here](https://pandas.pydata.org/pandas-docs/stable/).
- Special thanks to the open-source community for maintaining these useful tools and resources, which make projects like this possible.
