# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import sys
import time
import boto3
import logging
from botocore.client import Config
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

# boto3.set_stream_logger("")

# Set Variables and Parameter
my_profile_name = 'demo-user-1'
restore_sleep_time = 3600
restore_days = 1
restore_tier = 'Standard'
# Set AWS Region
my_region = 'us-east-2'

# Define Session
session = boto3.Session(profile_name=my_profile_name)


# initiate S3 resource
s3 = session.resource('s3', region_name=my_region)


""" Initiating Object Download from Amazon S3 Bucket """


def download_file_from_s3(mybucket, mykey):
    print("Please wait while I initiate object download from Amazon S3...")
    try:
        s3.Object(mybucket, mykey).download_file(file_name)
        print("Congratulations Object download is completed successfully!")
    except ClientError as e:
        print("Sorry, I encountered an error while downloading the Objects, details in a moment...")
        logger.error(e.response['Error'])
        if e.response['Error']['Code'] == 'InvalidObjectState':
            logger.error("The Object is in Glacier, This operation is not valid for the object's storage class")
            single_restore(mybucket, mykey)
        else:
            print("Object download Failed. Please check IAM and Resource Permissions..")
    # Catch all other Exceptions
    except Exception as e:
        logger.error(e)
        raise e


def single_restore(mybucket, mykey):
    obj = s3.Object(mybucket, mykey)
    if obj.storage_class == 'GLACIER':
        # Try to restore the object if the storage class is glacier and
        # the object does not have a completed or ongoing restoration
        # request.
        if obj.restore is None:
            print('Please wait while I Submit the restoration request: %s' % obj.key)
            obj.restore_object(RestoreRequest={'Days': restore_days, 'GlacierJobParameters': {'Tier': restore_tier}})
            print('I have submitted the restoration request successfully, please wait while your object is restored...')
            time.sleep(restore_sleep_time)
            single_restore(mybucket, mykey)
        # Print out objects whose restoration is ongoing
        elif 'ongoing-request="true"' in obj.restore:
            print('Restoration in-progress: %s' % obj.key)
            time.sleep(restore_sleep_time)
            single_restore(mybucket, mykey)
        # Print out objects whose restoration is complete
        elif 'ongoing-request="false"' in obj.restore:
            print('Restoration complete successfully for the object: %s' % obj.key)
            download_file_from_s3(mybucket, mykey)
    else:
        print("I just confirmed Object is NOT in Glacier Flexible Retrieval Storage Class, exiting......")


if __name__ == '__main__':
    # Specify parameters
    my_s3_bucket = input("Please enter your Amazon S3 Bucket name: ")
    my_s3_key = input("Please enter your Amazon S3 Key name:  ")
    file_name = my_s3_key
    # Download Object Now
    print("Welcome, I will assist you with downloading objects from Amazon S3, "
          "restoring from Glacier if needed...")
    download_file_from_s3(my_s3_bucket, my_s3_key)

## https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.restore_object
