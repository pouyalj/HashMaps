
import time

# Space Complexity: O(1)


class KV:
    
    def __init__(self):
        self.internal_map = {}
        self.key_time_map = {}
        
    # runtime: O(1)
    def set(self, key, value):
        timestamp = time.time()
        self.key_time_map[key] = timestamp
        key = key + str(timestamp)
        self.internal_map[key] = value
        return timestamp
    
    # runtime: O(1)
    def get(self, key, timestamp=0):
      if (timestamp == 0):
        max_time = self.key_time_map[key]
        return self.internal_map[key + str(max_time)]
      else:
        key = key + str(timestamp)
        return self.internal_map[key]

          

kv = KV()
t1 = kv.set('foo', 'bar') #100
time.sleep(2)# 102
t2 = kv.set('foo', 'new_bar')#103
print(kv.get('foo', t1)) # -> bar,

#internal_map = { 'foo': 'bar', 'foo2': 'bar2' }
# -> be able to store time alongside the key and value
#internal_map = { 'foo123': 'bar', 'foo2567': 'bar2' }
#key_time_map = { 'foo': '123', 'bar2': '567' }
