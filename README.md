# Snowball Uploader
A script to move a billions files to snowball efficiently
- Date: Feb 28, 2020
- Written by: Yongki Kim (hatsari@gmail.com)

## Introduction
[ graphic ]

*Snowball_uploader* is developed to move many of files efficiently to *Snowball* or *SnowballEdge* which is AWS's appliance to migrate petabyte files to S3. Especially, when there are millions of small files, it takes too long time to transfer them, then it will delay the project and cause high cost for lending the Snowball.  However, using *snowball_uploader*, you can shorten the transfer time.

## USAGE
### Prerequisites
- python3
- boto3
- awscli
### Execution
#### changing parameters
```python
bucket_name = "your-own-dest-seoul"
session = boto3.Session(profile_name='sbe1')
s3 = session.client('s3', endpoint_url='http://10.10.10.10:8080')
# or below
#s3 = boto3.client('s3', endpoint_url='https://s3.ap-northeast-2.amazonaws.com')
#s3 = boto3.client('s3', region_name='ap-northeast-2', endpoint_url='https://s3.ap-northeast-2.amazonaws.com', aws_access_key_id=None, aws_secret_access_key=None)
target_path = '/move/to/s3/orgin/'   ## very important!! change to your source directory
max_tarfile_size = 10 * 1024 ** 3 # 10GB
max_part_size = 300 * 1024 ** 2 # 300MB
min_part_size = 5 * 1024 ** 2 # 5MB
max_thread = 5  # max thread number
sleep_time = 3   # thread sleep time when reaching max threads
if os.name == 'nt':
    filelist_dir = "C:/Temp/fl_logdir_dkfjpoiwqjefkdjf/"  #for windows
else:
    filelist_dir = '/tmp/fl_logdir_dkfjpoiwqjefkdjf/'    #for linux
```
These parameters are crucial to run as you wish
-----
  - **bucket_name** : input your bucket name
  - **session = boto3.Session(profile_name='sbe1')**: input aws profile name
  - **target_path**: input directory path which you want to transfer to *Snowball*
    - if target_path = '/move/to/s3/origin/', it will move to s3://'bucket_name'/move/to/s3/origin/
    - if target_path = '.', it will move to s3://'bucket_name'/
    - so, it is very important where you execute the command *snowball_uploader* and fix the *target_path*
    - I suggest that you would test the script with sample data before applying to your data.
  - **max_tarfile_size**: tar file size which will be uploaded to *Snowball*
    - the value should be under 100 GB
    - *snowball_uploader* archives files to tar file in *Snowball*, and this tar file will be extracted automatically.
    - *Metadata={"snowball-auto-extract": "true"}*, this metadata is add to the tar file.
    - snowball limit ref: https://docs.aws.amazon.com/snowball/latest/developer-guide/batching-small-files.html
  - **max_part_size**: max multi part size, *Snowball* limits max-multi-part size to 512MB
      - this script used multi-part-upload feature of S3 to aggregate the files into one big tar file
      - snowball limit ref: https://docs.aws.amazon.com/snowball/latest/ug/limits.html
  - **min_part_size**: minimum multi part size, *Snowball* limits min-multi-part size to 5MB
      - ref: https://docs.aws.amazon.com/snowball/latest/ug/limits.html
  - **max_thread**: numbers of threads, *snowball_uploader* uses multiple threads to increase the upload speed
  - **sleep_time**: sleep time seconds, when thread count reaches max_thread count, it pauses for seconds of *sleep_time*
  - **filelist_dir**: where filelist file generated
    - /tmp/fl_logdir_dkfjpoiwqjefkdjf/ directory is fixed, and this directory removed and re-created whenever you run the script with *genlist* parameter.

#### genlist
``` shell
ec2-user> python3 snowball_uploader.py genlist
```

*genlist* parameter generates the manifest files containing original files and target files.
this parameter should be run before coping the files.

![genlist](https://recordit.co/joXk2dcJBB)

- files list to be transferred
files list split by the sum of files to fix the tar file size, max tar file size should be under 100GB.
``` shell
ec2-user> ls /tmp/fl_logdir_dkfjpoiwqjefkdjf
fl_1.yml fl_2.yml fl_3.yml fl_4.yml fl_5.yml
```

- the contents of file list
``` shell
ec2-suer> cat f1_1.yaml
./snowball_uploader_11_failed.py, ./snowball_uploader_11_failed.py
./success_fl_1.txt_20200224_165943.log, ./success_fl_1.txt_20200224_165943.log
./gen_filelist.py, ./gen_filelist.py
./success_fl_1.txt_20200224_224920.log, ./success_fl_1.txt_20200224_224920.log
./debug_part_10.log, ./debug_part_10.log
./error_fl_1.txt_20200224_224549.log, ./error_fl_1.txt_20200224_224549.log
./snowball_uploader_13_almost_success.py, ./snowball_uploader_13_almost_success.py
./success_fl_1.txt_20200224_173633.log, ./success_fl_1.txt_20200224_173633.log
```
  - the left is the original file name
  - the right is the target file name, if you want to change the file name on the S3, you can change it with *rename_file* method.
```python
def rename_file(org_file):
    target_file = org_file  ##
return target_file
```
#### cp_snowball

## HOW IT WORKS

## Conclusion
