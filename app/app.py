from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from sqlalchemy import text
from .infrastructure.db import get_db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    # 1行だけSQL叩いて疎通確認
    v = db.execute(text("select 1")).scalar_one()
    return {"db": "ok", "select_1": v}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
