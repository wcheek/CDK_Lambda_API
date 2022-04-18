import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lambda_model_predictions.lambda_model_predictions_stack import LambdaModelPredictionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_model_predictions/lambda_model_predictions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaModelPredictionsStack(app, "lambda-model-predictions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
