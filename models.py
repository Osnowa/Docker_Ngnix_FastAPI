from pydantic import BaseModel

class SWordAdd(BaseModel):
    '''Схема для добавления слова (то что присылает пользователь)'''
    word: str
    word_translate: str

class SWordGet(BaseModel):
    '''Схема для ответа (то что уходит в ответе пользователю)'''
    word: str