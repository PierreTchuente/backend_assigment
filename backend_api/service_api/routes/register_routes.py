class RegisterRoute:
    @staticmethod
    def register_api_routes(pyramid_config):
        pyramid_config.add_route("swagger", "/")
        pyramid_config.add_route("get_status", "/status")
