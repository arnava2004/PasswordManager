import dataBaseConfig
import rich
from rich.console import Console
from rich import print as printc
import sys
console = Console()


def config():
    # Create database
    db = dataBaseConfig.dataBaseConfig()
    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE pm")
    except Exception as e:
        printc("[red][!] An error occured while trying to create the DataBase")
        console.print_exception(show_locals = True)
        sys.exit(0)
    print("Database 'pm' created")

    #Time to create some tables

config()