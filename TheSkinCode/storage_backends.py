from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = 'static'
