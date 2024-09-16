#### MD5 CheckSum Calculator for S3 Bucket
by  Amit Sides
## Solution Proposal

AWS EKS (Kubernetes cluster) running microservices that pull from SQS new file in S3 (using EventBridge).

## Scenario
1. PUT FILE S3
   2. Trigger EventBridge
      3. Put into SQS
         2. Microservices Pull from SQS, Calculate Checksum and put in back into S3 Bucket.

#### Microservice for calculating MD5 of a file: Python + hashlib + Flask  
 https://docs.python.org/2/library/hashlib.html#module-hashlib https://docs.python.org/3/library/hashlib.html ) see Dockerfile
   2. docker build -t python-md5-microservice .
   3. docker run -p 5000:5000 python-md5-microservice

#### Activate S3 events to Amazon EventBridge
We'll have to trigger and Event everytime there is a new file upload. for this purpose I'll use AWS EventBridge https://aws.amazon.com/eventbridge/
Sign in to the AWS Management Console, and then open the Amazon S3 console.
In the Buckets list, choose the name of the bucket that you want to activate events for.
Choose Properties.
Navigate to the Event Notifications section and find the Amazon EventBridge subsection. Choose Edit.
For Send notifications to Amazon EventBridge for all events in this bucket, choose On.

#### Considerations for high availability and durability
Kubernetes will scale Pods of microservices using ReplicaSet,DeamonSet to make sure there is always a microservice ready to calculate MD5 Checksum.

## Terraform
See TF directory for bringing up AWS EKS + VPC + S3.

## HelmChart
Automating deployment of microservice to kubernetes use attached HelmChart.

## Testing
A user PUT file into Bucket which Triggers an EventBridge and put it into SQS, and then a Microservice PULL the file, calculate the CHECKSUM and PUT it back to S3.

## Summery
In this repo I've demonstrated how I brought up kubernetes on AWS which handles SQS Event Streaming from S3 PUTs in order to Calculate MD5 CheckSum and put it back into the Bucket.

## Further reading

https://repost.aws/knowledge-center/eventbridge-rule-monitors-s3
