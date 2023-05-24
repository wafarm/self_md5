.PHONY: coll

result: coll
	./gen_result.py

coll: prefix
	./gen_coll.py

self_md5: self_md5.c
	gcc self_md5.c -o self_md5 -O0

prefix: self_md5
	./gen_prefix.py
