from setuptools import setup

setup(
    name='dynamo_lock',
    packages=['dynamo_lock'],
    version='0.1.1',
    description='A lock implementation with AWS dynamo db',
    author='Julien Marechal',
    author_email='julien.marechal35@gmail.com',
    license='MIT',
    url='https://github.com/MarechJ/dynamodb-lock',
    download_url='https://github.com/MarechJ/dynamodb-lock/archive/0.1.1.tar.gz',
    keywords=['dynamo', 'dynamodb', 'aws', 'lock', 'distributed', 'locking'],
    install_requires=[
        "boto3>=1.4.5"
    ],
)
