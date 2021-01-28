#!/usr/bin/env python3

from boto3.session import Session
from decouple import config
from prettytable import PrettyTable

import os
import sys


def get_client():
    """
    Method to return a boto3 Session Client object for S3 service
    """
    return Session().client(
        's3',
        aws_access_key_id=config('S3_ACCESS_KEY'),
        aws_secret_access_key=config('S3_SECRET_ACCESS_KEY'),
    )


def list_buckets():
    """
    Method to print a list of S3 buckets we have access to
    """
    response = get_client().list_buckets()
    if buckets := response.get('Buckets'):
        print(f'Found {len(buckets)} buckets!')
        data = PrettyTable()
        for bucket in buckets:
            data.add_row(bucket.values())
        data.field_names = bucket.keys()
        print(data)
    else:
        print('No buckets found! Create one.')


def create_bucket():
    """
    Method to create an S3 bucket
    """
    bucket_name = input('Enter a name for your S3 bucket: ')
    try:
        get_client().create_bucket(Bucket=bucket_name)
        print(f'S3 bucket with name {bucket_name} has been succesfully created!')
    except Exception as e:
        print(e)


def delete_bucket():
    """
    Method to delete an S3 bucket
    """
    print("Here is a list of your buckets:-")
    list_buckets()
    bucket_name = input('\nEnter the name of the S3 bucket you wish to delete: ')
    try:
        get_client().delete_bucket(
            Bucket=bucket_name,
        )
        print(f'S3 bucket with the name {bucket_name} has been deleted!')
    except Exception as e:
        print(e)


def list_files(bucket_name: str = None):
    """
    Method to list the files in an S3 bucket
    """
    if bucket_name is None:
        print("Here is a list of your buckets:-")
        list_buckets()
        bucket_name = input('\nEnter the name of the S3 bucket you want a list files for: ')
    try:
        response = get_client().list_objects_v2(Bucket=bucket_name)
        if files := response.get('Contents'):
            data = PrettyTable()
            for file in files:
                data.add_row(file.values())
            data.field_names=file.keys()
            print(data)
        else:
            print('No files found in this bucket! Upload one.')
    except Exception as e:
        print(e)


def upload_file():
    """
    Method to upload a file to an S3 bucket
    """
    print("Here is a list of your buckets:-")
    list_buckets()
    bucket_name = input('\nEnter the name of the S3 bucket you to upload a file to: ')
    file_path = input(
        f'Enter the path to the file you wish to upload to {bucket_name}: '
    )
    if not os.path.isfile(file_path):
        print(f'{file_path} does not exist!')
    file_name = os.path.basename(file_path)
    key = (
        input(
            f'Enter the key (filename) you wish to upload {file_path} as (default {file_name}): '
        )
        or file_name
    )
    try:
        get_client().upload_file(
            Bucket=bucket_name,
            Filename=file_path,
            Key=key,
            ExtraArgs={'ACL': 'public-read'},
        )
        print(
            f'Your uploaded file {file_name} can be downloaded from https://{bucket_name}.s3.amazonaws.com/{key}'
        )
    except Exception as e:
        print(e)


def delete_file():
    """
    Method to delete a file from an S3 bucket
    """
    print("Here is a list of your buckets:-")
    list_buckets()
    bucket_name = input(
        '\nEnter the name of the S3 bucket you wish to delete a file from: '
    )
    print("Here is a list of files in the chosen S3 bucket:-")
    list_files(bucket_name)
    key = input(f'\nEnter the key (filename) you wish to delete from {bucket_name}: ')
    try:
        get_client().delete_object(
            Bucket=bucket_name,
            Key=key,
        )
        print(f'The file {key} has been deleted from S3 bucket {bucket_name}')
    except Exception as e:
        print(e)


def download_file():
    """
    Method to download a file from an S3 bucket
    """
    print("Here is a list of your buckets:-")
    list_buckets()
    bucket_name = input(
        '\nEnter the name of the S3 bucket you wish to download a file from: '
    )
    list_files(bucket_name)
    key = input(f'Enter the key (filename) you wish to download from {bucket_name}: ')
    file_path = (
        input(f'Enter the path you wish to download {key} to (default {key}): ') or key
    )
    try:
        get_client().download_file(Bucket=bucket_name, Key=key, Filename=file_path)
        print(f'Downloaded file {key} from S3 bucket {bucket_name} to {file_path}')
    except Exception as e:
        print(e)


if __name__ == '__main__':

    while True:
        # Prompt the user for an input
        prompt = """######## MENU ########
1: List buckets
2: Create a new bucket
3: Delete an existing bucket
4: List files in a bucket
5: Upload a file to a bucket
6: Delete a file from a bucket
7: Download a file from a bucket
Anything else to exit
Choice: """

        try:
            choice = int(input(prompt))
            print()
            if choice == 1:
                list_buckets()
            elif choice == 2:
                create_bucket()
            elif choice == 3:
                delete_bucket()
            elif choice == 4:
                list_files()
            elif choice == 5:
                upload_file()
            elif choice == 6:
                delete_file()
            elif choice == 7:
                download_file()
            else:
                break
            print()
        except ValueError:
            break
