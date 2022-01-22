class HashTable:
    
    def __init__(self):
        self.data = {}
        self.data_length = 100

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.data_length
        return hash

    def set(self, key, value):
        hash = self._hash(key)

        if not self.data.get(hash, None):
            self.data[hash] = []
        
        self.data[hash].append([key, value])

        return self.data

    def get(self, key):
        hash = self._hash(key)
        for i in self.data[hash]:
            if i[0] == key:
                return i[1]
        return None

hash_table = HashTable()
hash_table.set('grapes', 500)
print(hash_table.get('grapes'))

hash_table.set('apples', 15)
print(hash_table.get('apples'))