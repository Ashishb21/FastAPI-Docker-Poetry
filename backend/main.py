import uvicorn
from fastapi import FastAPI
from backend.api.app.routers import default
from backend.api.core.config import settings



def include_router(app):
    app.include_router(default.router)


def start_application():

    app=FastAPI(title=settings.APP_TITLE,version=settings.APP_VERSION)
    include_router(app)
    return app

app=start_application()

# if __name__=="__main__":
#     app=start_application()
#     #uvicorn.run(app,host=settings.APP_HOST,port=int(settings.APP_PORT))