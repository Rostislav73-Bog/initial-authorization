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
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get():
    return FileResponse("main.html")


@app.on_event('startup')
async def startup():
    await app.container.user_client().connect()
    print('connection db')


@app.on_event('shutdown')
async def shutdown():
    await app.container.user_client().disconnect()
    print('disconnecting db')

