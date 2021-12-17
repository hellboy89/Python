#!/usr/bin/env python
import boto3
print('\033c')


session = boto3.session.Session(profile_name='bigfile')

s3_client = session.client(
    service_name='s3',
    region_name='BR',
    endpoint_url='https://bigfile.brascloud.com.br'
)

print('Buckets')
print(s3_client.list_buckets())

print('')

print('Objects')
print(s3_client.list_objects(Bucket='teste'))

print()
