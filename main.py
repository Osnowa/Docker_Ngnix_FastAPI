from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from routers_words import router as router_words
from database.db import create_connections
from database.repositories.word_repositories import Word_Repositories

@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = await create_connections("/data/words.db")
    repo = Word_Repositories(conn)
    await repo.create_table()
    app.state.repo = repo
    yield
    await conn.close()


app = FastAPI(
    title = "Тестовый backand на RestAPI",
    description = "Демонстрация работы SQLite и Docker с пробросом портов и созданием тома для хранения данных\n Работа Nginx",
    version = "1.0.2",
    lifespan=lifespan
)

app.include_router(router_words)

#### Не нужно, так как запускаем проект через Docker при помощи uvicorn ###

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000)