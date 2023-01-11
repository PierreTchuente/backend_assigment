import binascii
import json

from pyramid.httpexceptions import (
    HTTPBadRequest,
    HTTPCreated,
    HTTPNotFound,
    HTTPOk,
)

from service_api.config import Config
from service_api.models.data import Data
from service_api.models.db_data import DbData

CONTENT_TYPE = "application/json"


class MessageController:
    def __init__(self):
        self.logger = Config.get_logger()

    def receive(self, message):
        self.logger.info(f"start receiving the message {message}")
        base_64_data = message.get("data")
        if base_64_data:
            try:
                data = Data.get_data_from_base64(base_64_data)
                result = DbData.create(data)
                self.logger.info(f"dumping the result from db {result}")
                message = "message data received and save successfully"
                response = HTTPCreated(
                    body=json.dumps({"error_code": 201, "message": message})
                )
                response.content_type = CONTENT_TYPE
                return response
            except binascii.Error:
                message = (
                    "The server could not comply with the request since"
                    " it is a malformed base 64 data in the message."
                )
                response = HTTPBadRequest(
                    explanation=message,
                    body=json.dumps({"error_code": 400, "message": message}),
                )
                response.content_type = CONTENT_TYPE
                return response
        else:
            message = "The data property is required"
            response = HTTPBadRequest(
                explaination=message,
                body=json.dumps({"error_code": 400, "message": message}),
            )
            response.content_type = CONTENT_TYPE
            return response

    def get_by_id(self, id_key):
        data = DbData.get_by_id(id_key)
        if not data:
            message = f"data with id {id_key} not found"
            response = HTTPNotFound(
                body=json.dumps({"error_code": 404, "message": message})
            )
            response.content_type = CONTENT_TYPE
            return response

        self.logger.info(f"data for id {id_key} is {data}")
        response = HTTPOk(body=json.dumps(data, default=str))
        response.content_type = CONTENT_TYPE
        return response

    def get_by_filter(self, page_number, page_size):
        list_data = DbData.get_list_data(page_number, page_size)
        self.logger.info(f"list of data {list_data}")
        result = {"data_list": list_data}
        response = HTTPOk(body=json.dumps(result, default=str))
        response.content_type = CONTENT_TYPE
        return response
