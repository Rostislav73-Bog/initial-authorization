from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from starlette.staticfiles import StaticFiles
import routes
from di_container import Container

def create_app() -> FastAPI:
    container = Container()
    container.config.from_yaml('config/config.yaml')
    container.wire(modules=[
        routes
    ])
    app = FastAPI()
    app.container = container
    app.include_router(routes.router)
    return app

app = create_app()
app.mount("/first_page", StaticFiles(directory="first_page"), name="first")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/home", StaticFiles(directory="home"), name="home")

@app.get("/", response_class=HTMLResponse)
async def first_page():
    return FileResponse("first_page/first.html")

@app.get("/main.html", response_class=HTMLResponse)
async def main():
    return FileResponse("main.html")

@app.get("/home/home.html", response_class=HTMLResponse)
async def get():
    return FileResponse("home/home.html")


@app.on_event('startup')
async def startup():
    await app.container.user_client().connect()
    print('connection db')


@app.on_event('shutdown')
async def shutdown():
    await app.container.user_client().disconnect()
    print('disconnecting db')

