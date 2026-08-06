import aiosqlite

async def create_connections(db_patch:str) -> aiosqlite.Connection:
    '''Создает соединение с базой данных'''
    conn = await aiosqlite.connect(db_patch)
    conn.row_factory = aiosqlite.Row # для обращения как к словарю
    return conn # возвращает соединение