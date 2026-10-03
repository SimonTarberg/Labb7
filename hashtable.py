class HashNode:
    """Noder till klassen"""
    def __init__(self, key="", data=None):
        """Ket är nyckeln som används vid hashningen
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
        hash_value=0
        "Metod för att hasha strängar"
        "Multiplicera med primtal för varje tecken"
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def store(self, key, data):
        """Stoppa in data med key i tabellen"""
        index = self.hashfunction(key)
        bucket = self.table[index]

        #Kolla om nyckeln redan finns
        for node in bucket:
            if node.key == key:
                node.data = data
                return

        #Om nyckeln inte fanns, lägg till en ny nod krocklistan
        bucket.append(HashNode(key, data))

    def search(self, key):
        """hämta objekt som finns lagrat med nyckeln key"""
        index = self.hashfunction(key)
        bucket =  self.table[index]

        #leta igenom krocklistan efter rätt nyckel
        for node in bucket:
            if node.key == key:
                return node.data

        raise KeyError(key)
