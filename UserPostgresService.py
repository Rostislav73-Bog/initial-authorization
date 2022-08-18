import asyncpg


class UserPostgresService:

    def __init__(self, url, table_name):
        self.url = url
        self.connection = None
        self.table_name = table_name

    async def __crate_table_users(self):
        await self.connection.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
            user_id serial PRIMARY KEY,
            email VARCHAR( 255 ) NOT NULL,
            login VARCHAR( 255 ) NOT NULL,
            password VARCHAR(255) NOT NULL,
            token VARCHAR( 255 )
            )
        ''')

    async def connect(self):
        self.connection = await asyncpg.connect(self.url)
        await self.__crate_table_users()

    async def disconnect(self):
        await self.connection.close()

    async def create_user(self, email: str, login: str, password: str, token_reponse: str):
        try:
            await self.connection.execute(f'''
                    INSERT INTO {self.table_name} (email, login, password, token)
                    VALUES ($1, $2, $3, $4);
                ''',email, login, password, token_reponse)
        except:
            None
