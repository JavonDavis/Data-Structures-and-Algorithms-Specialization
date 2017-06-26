# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def Swap(self, i, j):
      self._data[i], self._data[j] = self._data[j], self._data[i]
      self._swaps.append((i, j))
      
  def SiftUp(self, pos):
    if pos == 0: 
        return 
        
    if pos % 2 == 0:
        f = even_f
    else:
        f = odd_f
    parent_pos = f(pos)
    child = self._data[pos]
    parent = self._data[parent_pos]
    if child < parent:
       self.Swap(parent_pos, pos)
       self.SiftUp(parent_pos)
    
  def SiftDown(self, pos):
    left_child_pos = 2*pos + 1
    right_child_pos = 2*pos + 2
    left_child, right_child = None, None
    n = len(self._data)
    # print(left_child_pos, right_child_pos)
    if left_child_pos < n: 
        left_child = self._data[left_child_pos]
  
    if right_child_pos < n: 
        right_child = self._data[right_child_pos]

    if not left_child and not right_child:
        return
        
    if left_child and right_child:
        if left_child < right_child:
            if self._data[pos] > left_child:
                self.Swap(left_child_pos, pos)
                self.SiftDown(left_child_pos)
        else:
            if self._data[pos] > right_child:
                self.Swap(right_child_pos, pos)
                self.SiftDown(right_child_pos)
    elif left_child:
        if self._data[pos] > left_child:
            self.Swap(left_child_pos, pos)
            self.SiftDown(left_child_pos)
    else:
        if self._data[pos] > right_child:
            self.Swap(right_child_pos, pos)
            self.SiftDown(right_child_pos)

  def GenerateSwaps(self):
      # Turns self._data into heap and stores index swaps in self._swaps
    n = len(self._data)
    i = n//2
    while i > -1:
        self.SiftDown(i)   
        i -= 1
    # print(self._data)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()
    
def even_f(x):
    return (x - 2) // 2

def odd_f(x):
    return (x - 1) // 2

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
    
