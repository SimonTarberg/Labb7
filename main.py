class DictHash:
    def __init__(self):
        self._dict = {}

    def store(self, key, data): #dict innehåller data och key som nyckel.
        self._dict[key] = data

    def search(self, key):

        if key not in self._dict:
            raise KeyError(key)
        return self._dict[key]

    #---Extra frivilliga metoder ---

    def  __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        return key in self._dict

    #Testkörning___
class Drama:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return f"{self.name} (Betyg: {self.rating})"

if __name__ == "__main__":
    d_hash = DictHash()

    #Skapa drama
    d_hash.store("Squid Game", Drama("Squid Game", 8.0))
    d_hash.store("Crash Landing on You", Drama("Crash Landing on You", 8.7))

    #Sök efter ett drama som finns
    print("Söker efter squid game")
    print(d_hash.search("Squid Game"))

    if "Crash Landing on You" in d_hash:
        print("Crash Landing on You finns i tabellen!!!")
        print(d_hash["Crash Landing on You"])
    try: #det finns inte
        d_hash.search("Game of Thrones")
    except KeyError:
        print("Game of thrones finns inte i tabellen")