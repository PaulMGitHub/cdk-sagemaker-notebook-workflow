import json
import boto3

print('Loading function')

sagemaker = boto3.client('sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    nb_name = event['NotebookName']
    print(f'Stopping notebook instance with name: {nb_name}')
    sagemaker.stop_notebook_instance(NotebookInstanceName=nb_name)
    result = {}
    result['result'] = 'Success'
    return result