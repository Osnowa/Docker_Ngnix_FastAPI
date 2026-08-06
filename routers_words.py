from fastapi import APIRouter, status
from models import SWordGet, SWordAdd
from fastapi import FastAPI, Request


router = APIRouter(
    prefix="/words",
    tags=["words"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[SWordGet])
async def get_words(request: Request):
    '''Получить все слова'''
    return await request.app.state.repo.get_words()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_word(request: Request, word: SWordAdd):
    '''Добавить слово'''
    await request.app.state.repo.add_word(word.word, word.word_translate)