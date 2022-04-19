import aws_cdk as cdk

from cdk_lambda_stack.lambda_api_stack import LambdaAPIStack

app = cdk.App()
LambdaAPIStack(app, "ExampleLambdaAPIStack")

app.synth()
