__NOTE:__ This is not the full code. You have to download the VCL code from apache website and Install it by following the steps provided in Project report which is also attached with the code.

The code in __Code_v1__ is the most latest and working code.

Once you have Installed the VCL, please follow the below steps.
Steps to Integrate Cloud Burst logic in VCL. We have used Centos while running the VCL commands.

__NOTE:__ Report is also upload along with this code __cloud_burst_report.pdf__.

1. Install boto3 and mysql connector on the system using PIP.
    
    `$ yum -y install python-pip`
    
    `$ pip install boto3`

    `$ pip install mysql-connector==2.1.4`


2. Clone the above repo.
    
    `$ git clone https://github.ncsu.edu/engr-csc-547/2018FallCloudBursting.git`

3. copy all the files (aws_config.json,aws_delete.py,aws_delete_cron.py,aws_reservation.sql, delete.py, hello.py, launch.py) to folder __/var/www/cgi-bin/__

4. Copy Code_V1/php/requests.php to __/var/www/html/vcl-2.5/.ht-inc__.
    
    `$ cp Code_V1/php/requests.php /var/www/html/vcl-2.5/.ht-inc\requests.php`
5. Copy Code_V1/php/listaws.php to __/var/www/html/vcl-2.5/.ht-inc__.
    
    `$ cp Code_V1/php/listaws.php /var/www/html/vcl-2.5/.ht-inc\listaws.php`
6. Copy Code_V1/php/js/requests.js to __/var/www/html/vcl-2.5/.ht-inc/js/requests.js__

    `$ cp Code_V1/php/js/requests.js /var/www/html/vcl-2.5/.ht-inc/js/requests.js`

7. Run the DB command on your DB prompt. SQL create command is there in  aws_reservation.sql file.

    `$ mysql`
    
    `$ use vcl;`
    
    `$ create table aws_reservation(instance_id VARCHAR(50) NOT NULL,username varchar(50) NOT NULL,start_time datetime NOT NULL, end_time datetime NOT NULL, daterequested datetime NOT NULL default '0000-00-00 00:00:00',instance_username varchar(50) NOT NULL,password varchar(50) NOT NULL,dns_ip varchar(100),CONSTRAINT i_pk PRIMARY KEY(`instance_id`));`

8. Download the AWS key file which you created in your aws account and place it in your /var/www/cgi-bin/ with file name as __aws-ec2-keypair.pem__

9. From your AWS account update the aws_config.json file with latest credential. Update the value of **aws_access_key_id, aws_secret_access_key, aws_session_token**

10. Update your database credential in following file.
    
        aws_delete.py - Line NUmber 32

        aws_delete_cron.py - Line Number 6

        launch.py _ Line Number 47

        /var/www/html/vcl-2.5/.ht-inc\listaws.php - Line NUmber 65

