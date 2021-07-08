import sys
import time
import logging
import os
import requests
import datetime
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

logging.basicConfig(level=logging.ERROR)

def makecall(logLine):
    jsonLogLine= {
    "key":"",
    "station_profile_id":"",
    "type":"adif",
    "string":""
    }
    
    jsonLogLine['key']=APIKey
    jsonLogLine['station_profile_id']=station_profile_id
    jsonLogLine['string']=logLine
    
    resp = requests.post(LogBookServer+'/index.php/api/qso',json=jsonLogLine)
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S")+' Response:'+str(resp.status_code))
    print (resp)
    
def processLogfile(filename):
    inputfile=open(filename)
    logString=''
    
    for oneline in inputfile:
        if oneline[1:5].upper()=='CALL':
            logString=logString+oneline
    
    if logString !='':
        makecall(logString)

def _check_modification(filename):
        if(filename == filePath+"/wsjtx_log.adi"):
            #print ('modified:'+filename)
            processLogfile(filename)
 
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
       _check_modification(event.src_path)

 
if __name__ == "__main__":
    
    APIKey = os.environ.get('CloudlogAPIKey')
    station_profile_id = os.environ.get('ProfileID') # 1 for M0KHR
    filePath = os.environ.get('LogfilePath')
    LogBookServer= os.environ.get('LogBookServer')
    
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=filePath, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
