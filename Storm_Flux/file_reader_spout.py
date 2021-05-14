import os
from os.path import join
from time import sleep

from streamparse import Spout
import storm

class FileReaderSpout(storm.Spout):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._complete = False
        
        storm.logInfo("Spout instance starting...")

        # Initialize the file reader
        self.f = open(conf['datafile'], 'r')

    def nextTuple(self):
        # read the next line and emit a tuple for it
        sentence = self.f.readline()
        if sentence != "":
            storm.emit([sentence])
        else:
        # sleep for 1 second when the file is entirely read to prevent a busy-loop
            sleep(1.0)
# Start the spout when it's invoked
FileReaderSpout().run()