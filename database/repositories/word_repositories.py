import aiosqlite



class Word_Repositories:

    def __init__(self, conn: aiosqlite.Connection):
        self.conn = conn

    async def create_table(self):
        await self.conn.execute("""
            CREATE TABLE IF NOT EXISTS words (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                word TEXT, 
                word_translate TEXT
                )
            """)
        await self.conn.commit()

    async def add_word(self, word: str, word_translate: str):
        '''Добавляет слово в базу данных'''
        cursor = await self.conn.execute("INSERT INTO words (word, word_translate) VALUES (?, ?)", (word, word_translate))
        await self.conn.commit()

    async def get_words(self):
        '''Возвращает все слова из базы данных'''
        rows = await self.conn.execute("SELECT word FROM words")
        ROW_words = await rows.fetchall()
        return [{"word": row[0]} for row in ROW_words]

