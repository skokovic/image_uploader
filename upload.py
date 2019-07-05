import os
import sys
import time
import boto3
from dotenv import load_dotenv, find_dotenv

def main():
    """Searches for images and uploads them to s3"""
    if len(sys.argv) != 2:
        print('Provide the path to the root dir as the first argument!')
        exit(-1)
    path = sys.argv[1]

    load_dotenv(find_dotenv())

    s3 = boto3.client('s3', 
                    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'), 
                    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

    formats = ["jpg", "png", "heic"]

    for root, dirs, files in os.walk(path):
        all_images = find_images(files, root, formats)

        for f in all_images:
            print('Uploading ' + f + ' with mtime = ' + get_file_mtime(f))
            s3.upload_file(f, os.getenv('BUCKET_NAME'), get_file_mtime_key_name(f))


def get_file_mtime_key_name(file):
    """Return full filename with mtime key"""
    return get_file_mtime(file) + '/' + os.path.basename(file)

def get_file_mtime(file):
    """Return file last modified time"""
    return time.strftime('%Y-%m', time.gmtime(os.path.getmtime(file)))

def find_images(filenames: list, folder: str, formats: list):
    """Returns list of image abspaths for a folder if format in 'formats'"""
    all_images = [os.path.join(folder, file) for file in filenames if
                  file.lower().endswith(tuple(formats))]
    return all_images

if __name__ == "__main__": 
    main()