### Heyo JDB is in here ###
### this is the library ###
### save work: data -> Verifier -> JSON 
### load work: JSON -> Load -> data
### 2017. by anysz . Thanks for viewing :3
###############################
###     STABLE  VERSION     ###
###     Coding by anysz     ###
###############################

### Traceback version : 
###    Fixed error after deleting all data then add data

import json

class JDB:
    """	FlatDB JSON Access By anysz	"""
    """		 JSON TO DATABASE 		"""
    def __init__(self, file):
        self.dbfile = file # def file data

    def update(self, key, data): # root / dasar
        get = self.refresh()
        get[key] = data
        d = get
        try:
            json.dump(d, open(self.dbfile, "w"))
            self.refresh()
            return True
        except:
            return False

    def uadd(self, key, data): # implementasi
        get = self.isExist(key)
        if get == True:
            g = self.update(key, data)
            return g
        else:
            h = self.add(key, data)
            return h

    def delete(self, key): # root / dasar
        get = self.refresh()
        try:
            del get[key]
            d = get
            json.dump(d, open(self.dbfile, "w"))
            self.refresh()
            return True
        except:
            return False

    def add(self, key, data): # root / dasar
        d = {key: data}
        try:
            json.dump(d, open(self.dbfile, "a"))
            self.refresh()
            return True
        except:
            return False

    def addIN(self, key, data): # Implmentasi
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
			
    def refresh(self): # root / dasar
        g = open(self.dbfile, "r")
        h = g.read()
        g.close()
        g = open(self.dbfile, "w")
        j = h.replace("}{", ", ") # fix error
        j = j.replace("{, ", "{") # fix error
        j = j.replace("{{", "{") # fix error
        j = j.replace("}}", "}") # fix error
        g.write(j)
        g.close()
        g = open(self.dbfile, "r")
        kl = g.read()
        g.close()
        try:
            d = json.loads(str(kl))
            return d
        except:
            #pass
	        return "<FJDB Unexpected Error>"
	
### HELP FOR CLASS ### copyright anysz
# call Class				f = JDB("group.setting")
# to add data 				f.add(KEY, DATA)		||	return bool
# to edit data				f.update(KEY, DATA)		||  return bool
# to check data is exist 	f.isExist(KEY)			||  return bool
# to refresh data			f.refresh()				||  return string / dict
# to get specific data		f.get(KEY)				||  return string
# add data if not exist		f.addIN(KEY, DATA)		||  return bool
# remove data 				f.delete(KEY)			||  return bool
# add data, if exist update	f.uadd(KEY, DATA)		||  return bool

