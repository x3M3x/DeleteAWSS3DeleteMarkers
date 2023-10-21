import boto3



session = boto3.Session(
    aws_access_key_id= "",
    aws_secret_access_key= "",
    region_name= ""
)

bucket_name = ''
prefix = ''

s3_client = session.client('s3')

response = s3_client.get_bucket_versioning(Bucket=bucket_name)
if 'Status' in response and response['Status'] == 'Enabled':
    versions = s3_client.list_object_versions(Bucket=bucket_name, Prefix=prefix)
while True:
    print("Currently on",versions['NextKeyMarker'],"\n---------------------------")
    delete_keys = {'Objects': []}
    if 'DeleteMarkers' in versions:
        for delete_marker in versions['DeleteMarkers']:
            key = delete_marker['Key']
            version_id = delete_marker['VersionId']
            delete_keys['Objects'].append({'Key': key, 'VersionId': version_id})
    if delete_keys['Objects']:
        s3_client.delete_objects(Bucket=bucket_name, Delete=delete_keys)
        print(f"{len(delete_keys['Objects'])} delete markers found and deleted.")
    if not versions['IsTruncated'] or 'NextKeyMarker' not in versions:
        break  # Break the loop if there is no next page

    versions = s3_client.list_object_versions(Bucket=bucket_name, Prefix=prefix, KeyMarker=versions['NextKeyMarker'])

print("All delete markers have been checked and deleted if found.")