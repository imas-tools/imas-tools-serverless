from fastapi import FastAPI, __version__

from imas_tools.recochoku import query_metadata_for
from imas_tools.portal.calendar import fetch_articles_for_month, fetch_articles_for_today

app = FastAPI()

@app.get("/recochoku/metadata")
async def metadata(song_name: str, choice: int=0):
    return query_metadata_for(song_name, choice)


@app.get("/portal/calendar/month")
async def month_articles(year: int=0, month: int=0, brands: list[str]=[], subcategories: list[str]=[]):
    return fetch_articles_for_month(year, month, brands, subcategories) # type: ignore


@app.get("/portal/calendar/today")
async def today_articles(
    brands: list[str] = [], subcategories: list[str] = []
):
    return fetch_articles_for_today(brands, subcategories) # type: ignore
