import mysql.connector
import rich
from rich.console import Console
console = Console()

def dataBaseConfig():
    try:
        dataBase = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11212004"
        )
    except Exception as e:
        console.print_exception(show_locals=True)
    
    return dataBase
