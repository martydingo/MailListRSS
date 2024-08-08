from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def root():
    rssfeed = open("mailing-list.rss")
    return Response(content=rssfeed.read(), media_type="application/xml")
