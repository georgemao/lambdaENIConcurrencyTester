# lambdaENIConcurrencyTester
This project provides a sample that demostrates how concurrency impacts ENI scaling

First, deploy the provided sample Lambda function function. Use the provided SAM template (template.yaml) to package and deploy the function.
It is VPC enabled - be sure to edit the parameters to specify a Subnets and Security Groups that exist in your account.

`bash
sam package  --template-file template.yaml --s3-bucket [enter your s3 bucket here] --output-template-file packaged.yaml
`

`bash
sam deploy --template-file packaged.yaml --stack-name eniTestStack --capabilities CAPABILITY_IAM
`

Then, edit invoke.py to target the Lambda function you just deployed. Enter the concurrency you want to test.

`python
def handler():
    #Invoke the test lambda function that has VPC enabled
    response = client.invoke(
        FunctionName='eniTest',         #Specify your own lambda function here
        InvocationType='RequestResponse',
    )
    result = json.loads(response['Payload'].read())
    print (result)
`

Finally, execute the program:
`bash
python invoke.py
`
