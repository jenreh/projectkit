import logging

import reflex as rx
from starlette.types import ASGIApp

from appkit_commons.middleware import ForceHTTPSMiddleware
from appkit_user.authentication.pages import (  # noqa: F401
    azure_oauth_callback_page,
    github_oauth_callback_page,
)
from appkit_user.authentication.templates import navbar_layout
from appkit_user.user_management.pages import (  # noqa: F401
    create_login_page,
    create_profile_page,
)

from app.components.navbar import app_navbar
from app.pages.users import users_page  # noqa: F401

logging.basicConfig(level=logging.DEBUG)
create_login_page(header="ProjectKit")
create_profile_page(app_navbar())


@navbar_layout(
    route="/index",
    title="ProjectKit",
    description="The ProjectKit Homepage",
    navbar=app_navbar(),
    with_header=False,
)
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Welcome to ProjectKit!", size="9"),
            spacing="2",
            justify="center",
            margin_top="0",
        ),
    )


base_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Roboto+Flex:wght@400;500;600;700;800&display=swap",
    "https://fonts.googleapis.com/css2?family=Audiowide&family=Honk:SHLN@5&family=Major+Mono+Display&display=swap",
    "css/appkit.css",
    #    "css/styles.css",
    "css/react-zoom.css",
]

base_style = {
    "font_family": "Roboto Flex",
    rx.icon: {
        "stroke_width": "1.5px",
    },
}


# Middleware transformer for HTTPS redirect
def add_https_middleware(asgi_app: ASGIApp) -> ASGIApp:
    """Wrap the ASGI app with HTTPS redirect middleware."""
    return ForceHTTPSMiddleware(asgi_app)


app = rx.App(
    stylesheets=base_stylesheets,
    style=base_style,
    api_transformer=[add_https_middleware],
)
