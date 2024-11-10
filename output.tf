resource "aws_emrserverless_application" "validate_json_function" {
  // CF Property(Handler) = "app.lambda_handler"
  // CF Property(Runtime) = "python3.12"
  // CF Property(CodeUri) = "s3://aws-sam-cli-managed-default-samclisourcebucket"
  // CF Property(MemorySize) = 128
  // CF Property(Timeout) = 5
  // CF Property(Policies) = [
  //   "AWSLambdaBasicExecutionRole"
  // ]
  // CF Property(Events) = {
  //   ApiGatewayEvent = {
  //     Type = "Api"
  //     Properties = {
  //       Path = "/validatejson"
  //       Method = "get"
  //     }
  //   }
  // }
}

output "api_url" {
  description = "API Gateway endpoint URL"
  // Unable to resolve Fn::Sub with value: "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/ValidateJson" because Fn::Ref - ServerlessRestApi is not a valid Resource or Parameter.
}

output "validate_json_function" {
  description = "ValidateJson Lambda Function ARN"
  value = aws_emrserverless_application.validate_json_function.arn
}

output "validate_json_function_iam_role" {
  description = "Implicit IAM Role created for ValidateJson function"
  // Unable to resolve Fn::GetAtt with value: [
  //   "ValidateJsonFunctionRole",
  //   "Arn"
  // ] because 'Fn::GetAtt - Resource "ValidateJsonFunctionRole" not found in template.'
}
