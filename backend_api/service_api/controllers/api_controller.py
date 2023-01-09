from pyramid.httpexceptions import exception_response

from service_api.config import Config
from service_api.models.data import Data


class MessageController:
    def __init__(self):
        self.logger = Config.get_logger()

    def receive(self, message):  # sourcery skip: use-named-expression
        self.logger.info(f"start receiving the message {message}")
        base_64_data = message.get("data")
        if base_64_data:
            data = Data.get_data_from_base64(base_64_data)
            # We can use a db model here to write the data in tha database.
            self.logger.info(f"dumping the process data {data}")
            return {"status_code": 201}
        else:
            raise exception_response(400)
