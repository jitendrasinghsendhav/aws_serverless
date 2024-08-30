from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('Helloworld-handler')


class Helloworld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        response = {
                    "statusCode": 200,
                    "body": "hello from lambda"
                }
        return response


HANDLER = Helloworld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
