from fastapi import FastAPI, __version__

from imas_tools.recochoku import query_metadata_for
from imas_tools.portal.article import fetch_schedule_for_month, fetch_schedule_for_today

app = FastAPI()

@app.get("/recochoku/metadata")
async def metadata(song_name: str, choice: int=0):
    return query_metadata_for(song_name, choice)


@app.get("/portal/schedule/month")
async def month_schedule(
    year: int = 0, month: int = 0, brands: list[str] = [], subcategories: list[str] = []
):
    return fetch_schedule_for_month(year, month, brands, subcategories)  # type: ignore


@app.get("/portal/schedule/today")
async def today_schedule(brands: list[str] = [], subcategories: list[str] = []):
    return fetch_schedule_for_today(brands, subcategories)  # type: ignore
