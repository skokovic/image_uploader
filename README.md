# Uploader of photos to s3 bucket

## Dependencies
Python3.x with dotenv and boto3

## Environment variables
Create .env file with 3 env variables: AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, BUCKET_NAME

## Usage
Run the script with a single argument; path to the root directory of photos to upload

E.g. current dir
```
python3 upload.py .
```

## TODO
* pipenv / virtualenv
* shell command / CLI tool (interactive?)
* sync instead of upload (check if photos already exist in the bucket)