import os
import sys
import string
import random
import hashlib
import sys
from getpass import getpass

import dataBaseConfig

from rich import print as printc
from rich.console import Console

console = Console()


def config():
    # Create database
    db = dataBaseConfig.dataBaseConfig()
    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE pm")
    except Exception as e:
        console.print_exception(show_locals = True)
        sys.exit(0)
    printc("[green][+][/green] Database 'pm' created")

    #Time to create some tables
    # First Table will store the hash of the master password and the randomly generated device secret
    # Will convert this "local" quick storage with chrome API's chrome.storage.sync which stores inputted
    # entries locally until the browser quits, which will then be wiped out (in theory)
    queryFirstTable = "CREATE TABLE pm.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.execute(queryFirstTable)
    printc("[green][+][/green] Table 'secrets' created ")

    # Second table is where we will actually insert the new entries the user inputs (passwords)
    # passwords will be encypted and stored locally in chrome browser of user, will use chrome API again to store
    # in user's local computer, but due to the algorithm, if the passwords were to be leaked, they would be hard to decrypt
    # without the masterkey 
    queryEntriesTable = """CREATE TABLE pm.entries (sitename TEXT NOT NULL, url TEXT NOT NULL, 
    email TEXT NOT NULL, username TEXT, password TEXT NOT NULL)"""
    res = cursor.execute(queryEntriesTable)

    masterPassword = ""
    while True:
        masterPassword = getpass("Choose a MASTER PASSWORD: ")
        if masterPassword != getpass("Re-type MASTER PASSWORD: ") and masterPassword != "":
            break
        printc("[red][-] Please try again. [/red]")
    
    # Let's Hash the master password now
    hashedMasterPassword = hashlib.sha256(masterPassword.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of MASTER PASSWORD")