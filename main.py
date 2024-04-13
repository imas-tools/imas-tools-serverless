from fastapi import FastAPI, __version__

from imas_tools.recochoku import query_metadata_for

app = FastAPI()

@app.get("/recochoku/metadata")
async def metadata(song_name: str):
    return query_metadata_for(song_name)
