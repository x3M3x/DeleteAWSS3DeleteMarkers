# AWS S3 Delete Markers Remover

This Python script utilizes Boto3 to traverse an AWS S3 bucket prefix and delete all Delete markers found in all sub-prefixes under the main prefix. The primary use of this script is to facilitate the restoration of deleted files when versioning is enabled, especially in cases where files were inadvertently deleted.

Prerequisites

- Python 3.x
- Boto3 library

Important Note

- Ensure that you thoroughly understand the implications of deleting Delete markers in your S3 bucket, especially with regards to versioning. This script is intended for specific use cases and should be used with caution.
