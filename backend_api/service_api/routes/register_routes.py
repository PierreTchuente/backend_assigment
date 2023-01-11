class RegisterRoute:
    @staticmethod
    def register_api_routes(pyramid_config):
        """
        @param: pyramid_config: Configurator
        add route api to be registered on application startup
        """
        pyramid_config.add_route("swagger", "/")
        pyramid_config.add_route("get_status", "/status")
        pyramid_config.add_route("receive_message", "/receive/message")
        pyramid_config.add_route("get_by_id", "/data/{id}")
        pyramid_config.add_route("get_by_filter", "/data")
