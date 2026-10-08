class HashNode:
    """Noder till klassen"""
    def __init__(self, key="", data=None):
        """Key är nyckeln som används vid hashningen
        data är objekt(items) som hashas in"""
        self.key = key
        self.data = data

class Hashtable:
    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        #Skapar lista med tomma listor
        self.table = [[] for _ in range(size)]

    def hashfunction(self, key):
        """Metod för att hasha strängar.
        Multiplicera med primtal för varje tecken"""
        hash_value=0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def store(self, key, data):
        """Stoppa in data med key i tabellen"""
        index = self.hashfunction(key) # 1. räkna ut facket
        bucket = self.table[index] # 2. hämta krocklistan i facket

        #Kolla om nyckeln redan finns
        for node in bucket: # 3. gå igenom noderna som redan ligger där
            if node.key == key: #samma nyckel?
                node.data = data #    → ja: uppdatera värdet
                return


        bucket.append(HashNode(key, data)) # 4. ingen träff → lägg till sist i listan

    def search(self, key):
        """hämta objekt som finns lagrat med nyckeln key"""
        index = self.hashfunction(key)
        bucket =  self.table[index]

        #leta igenom krocklistan efter rätt nyckel
        for node in bucket:
            if node.key == key:
                return node.data

        raise KeyError(key)

    def __getitem__(self, key):
        """Gör att man kan skriva h[key]"""
        return self.search(key)

    def __contains__(self, key):
        """Gör att man kan skriva: if key in h"""
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def max_krock(self):
        """Längden på den längsta krocklistan (för att visa fördelningen)"""
        return max(len(bucket) for bucket in self.table)
