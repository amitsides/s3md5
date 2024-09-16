import json
import boto3
config = {
    'SQS_AUTH': {
        'SQS_REGION': 'SQS_REGION',
        'AWS_SECRET_ACCESS_KEY': 'AWS_SECRET_ACCESS_KEY',
        'AWS_ACCESS_KEY_ID': 'AWS_ACCESS_KEY_ID'
    },
    'SQS_NAME': 'my-standard-sqs'
}

class SQSClientManager:

    def __init__(self):
        self.auth = config.get('SQS_AUTH', None)
        self.queue_name = config.get('SQS_NAME', None)
        self.client = self.create_client()
        self.queue_url = self.get_queue_url()

    def create_client(self):
        client = boto3.client('sqs', region_name=self.auth['SQS_REGION'],
                              aws_secret_access_key=self.auth['AWS_SECRET_ACCESS_KEY'],
                              aws_access_key_id=self.auth['AWS_ACCESS_KEY_ID'])
        return client

    def get_queue_url(self):
        response = self.client.get_queue_url(QueueName=self.queue_name)
        return response.get('QueueUrl')

    def receive_message(self, **kwargs):
        response = self.client.receive_message(QueueUrl=self.queue_url, AttributeNames=['All'], MaxNumberOfMessages=1,
                                               MessageAttributeNames=['All'], WaitTimeSeconds=5)
        return response.get('Messages', list())

    def delete_message(self, receipt_handle):
        self.client.delete_message(QueueUrl=self.queue_url, ReceiptHandle=receipt_handle)

    def send_message(self, payload, attributes=None):
        self.client.send_message(QueueUrl=self.queue_url, MessageAttributes=attributes or dict(), MessageBody=payload)

if __name__ == '__main__':
    sqs_client = SQSClientManager()
    message = {'payload':'Test Message'}
    sqs_client.send_message(**message)
    print('MESSAGE SENT')

    messages = sqs_client.receive_message()
    for message in messages:
        print('Message: {}'.format(message['Body']))
        sqs_client.delete_message(message['ReceiptHandle'])

#     receipt_handle = 'RECEIPT HANDLE'
#     sqs_client.delete_message(receipt_handle)
#     print('MESSAGE DELETED')