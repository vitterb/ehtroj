import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler

def run(**args):
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    keyEvent = False
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_created(event):
        print(f"hey, {event.src_path} has been created!")
        keyEvent = True

    my_event_handler.on_created = on_created

    path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
            if keyEvent == True:
                path = os.getcwd() + '/data'
                for folder_path, folders, files in os.walk(path):
                    print(files)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()