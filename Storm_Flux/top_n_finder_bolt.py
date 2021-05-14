import heapq
from collections import Counter
import storm

class TopNFinderBolt(storm.BasicBolt):
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._N = int(conf['top-N'])  # length of word list e.g. 10
        self._heap = Counter()

    def process(self, tup):
        word = tup.values[0]
        count = int(tup.values[1])
        if word not in self._heap:
            self._heap[word] = count
        elif count > self._heap[word]:
            self._heap[word] = count
        
        top_lst = self._heap.most_common(self._N)
        top_N_words = [i[0] for i in top_lst]
        word_string = ", ".join(top_N_words)
         
        storm.emit(["top-N", word_string])
     
TopNFinderBolt().run()