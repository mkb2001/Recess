#DAY 7
#cONTEXT MANAGER
#MULTITHREADING AND MULTIPROCESSING


#CONTEXT MANAGER - is an defines a temporary context for a block of code.


# def open_file(filename):
#     """Open a file and return a context manager instance"""
#     file =open(filename, "r")
    
#     def __enter__():
#         return file
#     def __exit__():
#         file.close()
        
#         return __enter__,__exit__
    
# with open_file("my_file.txt") as f:
#     content = f.read()
    
    
    
    
#Multithreading and multiprocessing
#Multithreading is a technique where mulituplr threads are created with in a single process.
#Multiprocessing is a technique where multiple threads are created 

#Exampleof multithreading

# import threading

# def task(name):
#     print(f"Running task {name}")

# #Create multiple threads 
# threads = []
# for i in range(10):
#     t = threading.Thread(target=task,args=(f"Thread {i} ",))
#     threads.append(t)
#     t.start()
# #Wait for process to complete
# for t in threads:
#     t.join()
    
    
import threading 
import multiprocessing

def tesk(name):
    print(f"""
          Running task {name} on {threading.current_thread().name}
          with process {multiprocessing.current_process().name}
          """)
    
threads = []
for i in range(4):
    t = threading.Thread(target=tesk, args=(f"Thread {i}",))
    threads.append(t)
    t.start()
    
for t in threads: 
    t.join() 