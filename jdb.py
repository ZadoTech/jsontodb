import json

### Heyo JDB is in here ###
### this is the library ###
### save work: data -> Verifier -> JSON 
### load work: JSON -> Load -> data
### 2017. by anysz . Thanks for viewing :3

class JDB:
    """	FlatDB JSON Access By anysz	"""
    """		 JSON TO DATABASE 		"""
    def __init__(self, file):
        self.dbfile = file

    def update(self, key, data):
        get = refresh()
        get[key] = data
        d = get
        try:
            json.dump(d, open(self.dbfile, "w"))
            self.refresh()
            return True
        except:
            return False
    def delete(self, key):
        get = self.refresh()
        try:
            del get[key]
            d = get
            json.dump(d, open(self.dbfile, "w"))
            self.refresh()
            return True
        except:
            return False

    def add(self, key, data):
        d = {key: data}
        try:
            json.dump(d, open(self.dbfile, "a"))
            self.refresh()
            return True
        except:
            return False

    def addIN(self, key, data):
        ise = self.isExist(key)
        if ise != True:
            try:
                self.add(key, data)
                return True
            except:
                return False
        else:
            return False

    def isExist(self, key):
        get = self.refresh()
        try:
            res = get[key]
            self.refresh()
            return True
        except:
            return False
    def get(self, key):
        get = self.refresh()
        try:
            ret = get[key]
            self.refresh()
            return ret
        except:
            return "<FJDB Not Exist>"

    def refresh(self):
        g = open(self.dbfile, "r")
        h = g.read()
        g.close()
        g = open(self.dbfile, "w")
        g.write(h.replace("}{", ", "))
        g.close()
        g = open(self.dbfile, "r")
        kl = g.read()
        try:
            d = json.loads(str(kl))
            return d
        except:
	        return "<FJDB Unexpected Error>"
