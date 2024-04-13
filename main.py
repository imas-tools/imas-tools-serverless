from time import time
from fastapi import FastAPI, __version__

# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse
from imas_tools.recochoku import query_metadata_for

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/recochoku/metadata")
async def metadata(song_name: str):
    return query_metadata_for(song_name)
