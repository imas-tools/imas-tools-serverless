from typing import Optional, List

from fastapi import FastAPI, Query

from imas_tools.recochoku import query_metadata_for
from imas_tools.portal.interfaces import BRAND_CODE, SUBCATEGORY_CODE
from imas_tools.portal.article import fetch_schedule_for_month, fetch_schedule_for_today
from imas_tools.story.gakuen_parser import parse_messages

app = FastAPI()


@app.get("/recochoku/metadata")
async def metadata(song_name: str, choice: int = 0):
    return query_metadata_for(song_name, choice)


@app.get("/portal/schedule/month")
async def month_schedule(
    year: int = 0,
    month: int = 0,
    brands: Optional[List[BRAND_CODE]] = Query([]),
    subcategories: Optional[List[SUBCATEGORY_CODE]] = Query([]),
):
    return fetch_schedule_for_month(year, month, brands, subcategories)  # type: ignore


@app.get("/portal/schedule/today")
async def today_schedule(
    brands: Optional[List[BRAND_CODE]] = Query([]),
    subcategories: Optional[List[SUBCATEGORY_CODE]] = Query([]),
):
    return fetch_schedule_for_today(brands, subcategories)  # type: ignore


from pydantic import BaseModel


class Item(BaseModel):
    story_txt: str


@app.post("/story/gakuen_parser")
async def gakuen_parser(item: Item):
    parsed = parse_messages(item.story_txt)
    # print(parsed)
    return parsed
