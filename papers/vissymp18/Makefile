# pandoc --print-default-data-file reference.docx > smartnova18.docx

MARKDOWN=vsj18.md
DOCX=vsj18-wakita.docx

$(DOCX): $(MARKDOWN) etc/smartnova18.docx
	pandoc \
	  --bibliography=library.bib \
	  --reference-doc=etc/smartnova18.docx \
	  --filter pandoc-citeproc $(MARKDOWN) \
	  --csl=etc/apa.csl \
	  --standalone \
	  --output $@
	#pandoc --bibliography=library.bib --reference-doc=etc/smartnova18.docx --filter pandoc-citeproc --filter pandoc-tablenos $(MARKDOWN) -s -o $@

clean:
	rm -f $(DOCX)
