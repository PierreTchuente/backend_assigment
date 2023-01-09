from pyramid.response import Response
from pyramid.view import view_config

from service_api.config import Config
from service_api.controllers.api_controller import MessageController

logger = Config.get_logger()
message_controller = MessageController()


@view_config(route_name="swagger", request_method="GET")
def swagger(request):
    logger.info(f"logging the request {request}")
    return Response("OK")


@view_config(route_name="get_status", request_method="GET")
def get_status(request):
    return {"ok": True}


@view_config(route_name="receive_message", request_method="POST")
def receive_message(request):
    payload = request.swagger_data["payload"]
    return message_controller.receive(payload.get("message"))
