import hashlib

def h1(clave):
	h = hashlib.sha256(clave.encode())
	return int(h.hexdigest(), base=16)
