# lambdaENIConcurrencyTester
This project provides an example that demostrates how concurrency impacts ENI scaling.

First, deploy the provided sample Lambda function function. Use the provided SAM template (template.yaml) to package and deploy the function.
It is VPC enabled, so be sure to edit the parameters and specify a *Subnets* and *Security Groups* that exist in your account.

```bash
sam package  --template-file template.yaml --s3-bucket [enter your s3 bucket here] --output-template-file packaged.yaml
`

```bash
sam deploy --template-file packaged.yaml --stack-name eniTestStack --capabilities CAPABILITY_IAM
`

Then, edit invoke.py to target the Lambda function you just deployed.

```python
def handler():
    #Invoke the test lambda function that has VPC enabled
    response = client.invoke(
        FunctionName='eniTest',         #Specify your own lambda function here
        InvocationType='RequestResponse',
    )
    result = json.loads(response['Payload'].read())
    print (result)
```

Configure the level of concurrency you want to test:

```python
# Number of concurrent threads to execute
MAX_WORKERS = 50
# Number of total requests to simulate
INVOKE_TIMES = 50 
`

Finally, execute the program:
```bash
python invoke.py
`
