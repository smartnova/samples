.SUFFIX: .js .html .md

JS       := $(wildcard *.js)
HTML     := $(addsuffix .html, $(basename $(JS)))

all: $(HTML)

clean:
	rm -f *.html

%.html: %.js
	echo "<script src=\"$^\"></script>" | \
	  pandoc \
	    --standalone \
	    --from markdown \
	    --to html \
	    --css lib/common.css \
	    --include-in-header lib/0-header \
	    --include-before-body lib/0-body \
	    --metadata=title:"$^" \
	    --output $@
