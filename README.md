# Spotify Music Data Into S3 Bucket By Using ETL Data Pipeline with Apache Airflow
## Project Overview
This project demonstrates an **ETL (Extract, Transform, Load)** pipeline built using **Apache Airflow**, which automates the process of extracting data from the **Spotify API**, transforming the data with **Python**, and loading it into an **S3 bucket** for storage. The pipeline is scheduled and managed using **Airflow DAGs**.

## Key Features:
- **Extracts data** from Spotify API, including data such as songs, albums, or playlists.
- **Transforms the data** into the desired format (e.g., CSV or JSON) using custom Python scripts.
- **Loads the transformed data** into an S3 bucket for further analysis or use.
- **Orchestrates the entire ETL workflow** using Apache Airflow for scheduling and automation.

## Architecture:
![project architecture](ETL.jpg)

## Technology Used:
1.Programming Language - Python

2.AWS Cloud Service Platform
  - EC2 Instance
  - S3 Bucket

3.Apache Airflow(Workflow Orchestration)

## Installation

### Prerequisites
1. Python Interpreter
2. Apache Airflow 
3. Spotify API
   -Make One API Using This Link-***https://developer.spotify.com/dashboard***
4.AWS Account

## Steps to Set Up
**1.Spotify API**

-Create Spotify Account And Login to https://developer.spotify.com/dashboard.

-Create App add name,redirect url and setup app.

-Then get Client ID,Client secret It use to Authenticate Spotify API to fetch Data.

**2.EC2 Instance**

-Go to AWS login to console.

-Make EC2 Instance and Connect to It and Run Following Commands To setup EC2.

-Commands:

 -sudo apt-get update
 
 -sudo apt install python3-pip 
 
 -sudo pip install apache-airflow
 
 -sudo pip install pandas
 
 -sudo pip install s3fs
 
 -sudo pip install spotipy

 **3.Start Apache Airflow**

-Run the Command on ec2 instance **airflow standalone**

-This will setup Airflow and get username and password and airflow running on by default port.

-Login to airflow uisng username and password and get access to dashboard.

