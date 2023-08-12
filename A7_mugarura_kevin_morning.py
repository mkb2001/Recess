# Qn 1
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except IOError as e:
            
            print(f"Error opening file: {str(e)}")
            return None

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            try:
                self.file.close()
            except IOError as e:
               
                print(f"Error closing file: {str(e)}")
        if exc_type is not None:
            
            print(f"Exception occurred: {str(exc_value)}")
            return False
        return True

with FileManager('recess.txt', 'r') as file:
    if file:
        try:
            content = file.read()
            print(content)
        except IOError as e:
            
            print(f"Error reading file: {str(e)}")
            
#QN 2
import psycopg2
"""Here I used my postgres database installed on my machine"""
class DatabaseContextManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return self.connection
        except psycopg2.Error as e:
          
            print(f"Error connecting to database: {str(e)}")
            return None

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.connection:
            try:
                self.connection.close()
            except psycopg2.Error as e:
        
                print(f"Error disconnecting from database: {str(e)}")
        if exc_type is not None:
    
            print(f"Exception occurred: {str(exc_value)}")
            return False
        return True


with DatabaseContextManager(dbname='postgres', user='kevin', password='1234', host='localhost', port='5432') as conn:
    if conn:
        try:
            cursor = conn.cursor()
     
            cursor.execute("CREATE TABLE IF NOT EXISTS assignment (id SERIAL PRIMARY KEY, name VARCHAR(50))")
            cursor.execute("INSERT INTO assignment (name) VALUES ('context_manager_assignment')")
            conn.commit()
            cursor.execute("SELECT * FROM assignment")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except psycopg2.Error as e:
           
            print(f"Error executing database operation: {str(e)}")
            
#Qn 3            
import time
from threading import Thread
from multiprocessing import Process

def task(job, runing_time):
    print(f"Function will run for {runing_time} seconds.")
    time.sleep(runing_time)
    task_name = job.__name__
    print(f"{task_name} finished executing.")

def task1():
    print("started execution.")
    time.sleep(3)
    print("finished execution.")


thread = Thread(target=task, args=(task1, 5))
thread.start()


process = Process(target=task, args=(task1, 7))
process.start()

thread.join()
process.join()
