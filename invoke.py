# This PY Script should be invoked on the command line, not in a lambda function
# ie: "python invoke.py"

from concurrent import futures
import json
import os
import boto3

# Number of concurrent threads to execute
MAX_WORKERS = 50
# Number of total requests to simulate
INVOKE_TIMES = 50 

client = boto3.client('lambda')

def handler():
    #Invoke the test lambda function that has VPC enabled
    response = client.invoke(
        FunctionName='eniTest',
        InvocationType='RequestResponse',
    )
    result = json.loads(response['Payload'].read())
    print (result)


# concurrently call lambda function
with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
    for i in range(INVOKE_TIMES):
        pool.submit(handler)