import mysql.connector
from mysql.connector import Error
class DatabaseConnectoin:
    __instance_connection=None
    def __new__(cls,host_name,data_base_name, user_name, user_password,port):
        if cls.__instance_connection is None:
            cls.__instance_connection=super().__new__(cls)
        return cls.__instance_connection
    def __init__(self,host_name,data_base_name, user_name, user_password,port):
        if not hasattr(self, '_initialized') or not self._initialized:
    #connection = None
            try:
                self.__instance_connection = mysql.connector.connect(
                    host=host_name,
                    database=data_base_name,
                    user=user_name,
                    passwd=user_password,
                    port=port
                )
                self._initialized = True
                print("Connection to MySQL DB successful")
            except Error as e:
                print(f"The error '{e}' occurred")

    #return connection

#connection = create_connection("localhost", "root", "LIND4049100912mahdi",3307)
#print(connection)
    def describe_table(self, table_name):
        cursor = self.__instance_connection.cursor()
        try:
            query = f"DESCRIBE {table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            print(f"Description of the table `{table_name}`:")
            for row in result:
                print(row)
        except Error as e:
            print(f"The error '{e}' occurred")
            
    def get_connection(self):
        return self.__instance_connection

    def close_connection(self):
        print(f"Connection closed.")
        self.__instance_connection = None
        
if __name__ == "__main__":
    print("hello")
    connection = DatabaseConnectoin("localhost", "messenger", "root", "LIND4049100912mahdi", 3307)
    print(connection.get_connection())
    
    connection.describe_table("users")
    
    connection2 = DatabaseConnectoin("localhost", "test", "root", "LIND4049100912mahdi", 3307)
    connection2.describe_table("events")

       # connection.close()