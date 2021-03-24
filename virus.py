from time import sleep
from platform import *
import os

while True:
    try:
        if platform.system == "windows":
            os.system("shutdown /s /t 1")
        else:
            print("Su sistema operativo no es windows")
    
    except Exception as error:
        print(error)
    except OSError:
        print("hay un error que impide la ejecución del programa...")
            
 