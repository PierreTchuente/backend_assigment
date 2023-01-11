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


@view_config(route_name="get_by_id", request_method="GET")
def get_by_id(request):
    id_key = int(request.swagger_data["id"])
    return message_controller.get_by_id(id_key)


@view_config(route_name="get_by_filter", request_method="GET")
def get_by_filter(request):
    page_number = int(request.swagger_data["page_number"])
    page_size = int(request.swagger_data["page_size"])
    return message_controller.get_by_filter(page_number, page_size)
