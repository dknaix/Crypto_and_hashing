import hashlib as Hash
import base64
txt=input("\nEnter text Here:")
str(txt)
enc=str.encode(txt)
type(txt)

md5=Hash.md5(enc).hexdigest()
sha256=md5=Hash.sha256(enc).hexdigest()
sha1=md5=Hash.sha1(enc).hexdigest()

pyhash=str(hash(enc))
b64=str(base64.encodebytes(enc))
b64s=str(base64.encodestring(enc))


#print("Py Hash: "+pyHash)
print()
print("MD5   : "+md5)
print("Sha256: "+ sha256)
print("Sha1  : "+ sha1)
print("PyHash: "+pyhash)
print("B64   : "+b64)
print("b64str:"+b64s)
print()
input("Exit??")
