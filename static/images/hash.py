import hashlib
albumid = 4
filename = 'space_OrionNebula.jpg'
m = hashlib.md5()
m.update(str(albumid))
m.update(filename)
print m.hexdigest()
