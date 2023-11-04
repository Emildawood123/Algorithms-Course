# A simple implementation of Priority Queue
# using Queue.
import heapq


class HeapNode:

  def __init__(self, data, freq):
    self.data = data
    self.freq = freq
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.freq < other.freq
  
class Huffman:
    def __init__(self, massage):
        self.initial = chr(0)
        self.codes = {}
        freqHash = {}
        for char in massage:
            if (char in freqHash):
               freqHash[char] += 1
            else:
               freqHash[char] = 1
        self.minHeap = []
        for key, value in freqHash.items():
          newNode = HeapNode(key, value)
          heapq.heappush(self.minHeap, (newNode.freq, newNode))
        print(freqHash)
        while len(self.minHeap) > 1:
          left_freq, left_node = heapq.heappop(self.minHeap)
          right_freq, right_node = heapq.heappop(self.minHeap)
          newFreq = left_freq + right_freq
          top = HeapNode(self.initial, newFreq)
          top.left = left_node
          top.right = right_node
          heapq.heappush(self.minHeap, (newFreq, top))
        print(self.minHeap)
        self.generateCodes(self.minHeap[0][1], "")
        print(self.minHeap)
    def generateCodes(self, node, code):
      if node is None:
        return
      if node.data != self.initial:
        self.codes[node.data] = code
      self.generateCodes(node.left, code + "0")
      self.generateCodes(node.right, code + "1")

if __name__ == "__main__":
    msg = "eemil edawood henwaye"
    code = Huffman(msg)
    print(code.codes)   
    
