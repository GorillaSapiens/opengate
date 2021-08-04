all:
	-killall graph.pl
	-killall neato
	./reap.pl
	./graph.pl > data/foo1.dot
	neato -n data/foo1.dot > data/foo2.dot
	egrep "^#" data/foo1.dot | sed "s/^#//g" > data/foo3.dot
	egrep -v "^}" data/foo2.dot > data/foo4.dot
	cat data/foo4.dot data/foo3.dot > data/foo5.dot
	echo "}" >> data/foo5.dot
	neato -n -o data/foo6.dot data/foo5.dot
	neato -n -Tsvg -o new_image.svg data/foo6.dot
	mv new_image.svg image.svg
#	neato -n -Tpng -o new_image.png data/foo6.dot
#	mv new_image.png image.png
#	neato -n -Tgif -o new_image.gif data/foo6.dot
#	mv new_image.gif image.gif

all2:
	./graph.pl > data/foo1.dot
	circo data/foo1.dot > data/foo2.dot
	neato -n -Tpng -o image.png data/foo2.dot
	neato -n -Tgif -o image.gif data/foo2.dot

clean:
	rm data/foo*
