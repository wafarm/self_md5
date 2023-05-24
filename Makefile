self_md5: self_md5.c
	gcc self_md5.c -o self_md5 -O0

prefix: self_md5
	./gen_prefix.py

clean:
	rm -f prefix
	rm -f self_md5
	rm -f self_md5.o self_md5.s
	rm -f test0 test1 xaa