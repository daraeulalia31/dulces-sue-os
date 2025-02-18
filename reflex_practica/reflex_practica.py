import reflex as rx
from .components.navbar import navbar
from .components.seccion import seccion
def index()->rx.components:
  return rx.vstack(
    navbar(),
    seccion(),
    bg="#fde7fa",
    height="100vh",
    align="center"
  )
app=rx.App()
app.add_page(index)