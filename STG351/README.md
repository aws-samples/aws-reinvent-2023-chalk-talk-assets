# Optimize performance and cost for Amazon S3 Glacier restores

### _Description_

**Demo App Code** for **Re-Invent 2023 STG 351 Optimize performance and cost for Amazon S3 Glacier restores** - Downloads the specified [object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html) in [Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) to local directory, will automatically issue restore for object in [Glacier Flexibe Retrieval](https://aws.amazon.com/s3/storage-classes/?nc=sn&loc=3), monitors the restore state by polling and downloads the object when restore is completed


#### _**Customer Value**_

The code show cases a way to download objects from Amazon S3 to local directory when an object is in synchronous storage classes (Standard, Standard-IA, One-Zone-IA, Glacier Instant retrieval, S3 Intelligent tiering access tiers) or asynchronous storage class (Glacier Flexible Retrieval). Customers can build on this to create applications or code that can download object from any S3 Storage class.


#### _**Workflow:**_

1. Archived Object in Glacier Flexible Retrieval
2. Demo app issues Get request
3. Error is returned
4. A Standard restore request is submitted
5. Demo app sleeps
6. App issues Head to check restore status
7. Demo app issues a successful Get request



#### _**Configuration:**_

The code contains some predefined parameters that can be customized:


* Retrieval speed (Tier) is Standard
* Restore days (Days)
* Profile name (profile_name) 
* Region (my_region)
* Sleep/wait time (restore_sleep_time)
* Supported Archive Storage class (obj.storage_class)



#### _Requirements:_

* [Python](https://www.python.org/downloads/)
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
* [AWS Account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)
* [IAM user Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) with [s3:Restoreobject,](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) [s3:GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)and [s3:ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) permissions
* [Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html)
* Object in [Glacier Flexible Retrieval](https://aws.amazon.com/s3/storage-classes/?nc=sn&loc=3)



#### _How to use:_

* Download the code to a local directory
* Confirm you have Python [python —version ] and Boto3 installed [pip list]
* Run the code with “python demo-app-1.py”
* The code will prompt for the S3 bucket name and object name and then start the download and optional restore process


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

