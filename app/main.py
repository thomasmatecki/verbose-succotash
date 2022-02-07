"""
  main.py
"""
from os import getenv, path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

CSS_DIRECTORY = path.realpath(getenv("CSS_DIRECTORY"))
TEMPLATE_DIRECTORY = path.realpath(getenv("TEMPLATE_DIRECTORY"))

app = FastAPI()

app.mount("/css", StaticFiles(directory=CSS_DIRECTORY), name="static")
templates = Jinja2Templates(directory=TEMPLATE_DIRECTORY)


@app.get("/items/{id_}", response_class=HTMLResponse)
async def read_item(request: Request, id_: str):
    """"""
    return templates.TemplateResponse("item.html", {"request": request, "id": id_})


@app.get("/config")
def read_root():
    """
    Foo
    """
    return {"css": CSS_DIRECTORY, "templates": TEMPLATE_DIRECTORY}


#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}
#
