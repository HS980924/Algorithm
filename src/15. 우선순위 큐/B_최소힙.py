def heapPush(heap:list, value):
    heap.append(value)
    siftDown(heap)
    
def siftDown(heap:list):
    startPos = 0
    pos = len(heap)-1
    newValue = heap[pos]
    
    while startPos < pos:
        parentPos = (pos-1) // 2
        parentValue = heap[parentPos]
        if newValue < parentValue:
            heap[pos] = parentValue
            pos = parentPos
            continue
        break
    heap[pos] = newValue

def heapPop(heap:list):
    lastValue = heap.pop()
    if heap:
        minValue = heap[0]
        heap[0] = lastValue
        siftUp(heap,0)
        return minValue
    return lastValue   

def siftUp(heap:list, pos):
    endPos = len(heap)
    childpos = 2*pos + 1
    newValue = heap[pos]
    
    while childpos < endPos:
        rightpos = childpos + 1
        if rightpos < endPos and heap[rightpos] < heap[childpos] :
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
        
    heap[pos] = newValue
    siftDown(heap)
    
N = int(input())
heap = []

for i in range(N):
    value = int(input())
    
    if value > 0:
        heapPush(heap, value)
    else:
        if heap:
            print(heapPop(heap))
        else:
            print(0)

