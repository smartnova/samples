# pandoc --print-default-data-file reference.docx > smartnova18.docx

vsj18-wakita.docx: vsj18.md etc/smartnova18.docx
	pandoc --bibliography=library.bib --reference-doc=etc/smartnova18.docx --filter pandoc-citeproc vsj18.md -s -o $@
