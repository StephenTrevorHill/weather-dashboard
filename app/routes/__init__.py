# app/routes/__init__.py


def setup_routes(app):
    from .cities_route import setup_routes as setup_city_picker_routes
    from .city_weather_route import setup_routes as setup_city_weather_routes
    from .countries_route import setup_routes as setup_country_picker_routes
    from .index_route import setup_routes as setup_index_routes

    setup_index_routes(app)
    setup_city_weather_routes(app)
    setup_country_picker_routes(app)
    setup_city_picker_routes(app)
