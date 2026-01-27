from langgraph.checkpoint.postgres import PostgresSaver
from psycopg_pool import ConnectionPool
from typing import Optional

class DatabaseManager:
    """
    Docstring for DatabaseManager
    """
    def __init__(self):
        """
        """
        self.pool: Optional[ConnectionPool] = None

    def initialize(self, connection_string: str):
        """
        Docstring for initalize
        
        :param self: Description
        :param connection_string: Description
        :type connection_string: str
        """
        self.pool = ConnectionPool(
            conninfo= connection_string,
            max_size=20,
            kwargs={"autocommit" : True, "prepare_threshold" : 0}
        )

        #set up checkpointer
        with self.pool.connection() as conn:
            saver = PostgresSaver(conn)
            saver.setup()
    
    def close(self):
        """
        Docstring for close
        
        :param self: Description
        """
        if self.pool:
            self.pool.close()

    def get_saver(self) -> PostgresSaver:
        """
        Docstring for get_saver
        
        :param self: Description
        :return: Description
        :rtype: PostgresSaver
        """
        if not self.pool:
            raise RuntimeError("Database not initialized")
        return PostgresSaver(self.pool)
    
db_manager = DatabaseManager()