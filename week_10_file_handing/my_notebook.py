
import json
import re
import logging
from datetime import datetime
from pathlib import Path


logging.basicConfig(level=logging.INFO , format ="%(asctime)s - %(levelname)s - %(message)s")

NOTE_FILE = Path("notes.json")

def load_notes()->list:
    if not NOTE_FILE.exists():
        logging.warning(f"Notes file {NOTE_FILE } not found")
        return []

    with open(NOTE_FILE ,"r",encoding="utf-8")as f:
        logging.info(f"Notes file {NOTE_FILE } loaded")
        return json.load(f)

def save_notes(text: str)-> None:
    notes = load_notes()
    note = {"time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S") , "text":text}
    notes.append(note)

    with open(NOTE_FILE , "w" , encoding="utf-8") as f:
        json.dump(notes, f, indent=4)
    logging.info(f"Note saved to {NOTE_FILE }")

def search_notes(keyword:str)->list:
    notes = load_notes()

    # matches = []
    # for note in notes:
    #     text = note["text"]
    #     match = re.search(keyword , text , re.IGNORECASE)
    #     matches.append(match)


    return [note for note in notes if re.search(keyword, note["text"], re.IGNORECASE)]


if __name__ =="__main__":
    save_notes("This Is My Daily Rounting Notebook")
    save_notes("My Mobile Number Is 1122334455")
    save_notes("This Is My Personal Notebook So If You Opended Then Please Close It.")

    search_result = search_notes("1122334455")
    print(search_result)