all: docx

HEADER=vsj18-header.md
MACRO=macros.tex
MARKDOWN=md/*.md
INPUTS=$(HEADER) $(MACRO) $(MARKDOWN)
DOCX=vsj18-wakita.docx
HTML=vsj18-wakita.html

define pandoc
  pandoc \
    --from markdown+latex_macros \
    --filter pandoc-citeproc \
    --bibliography=library.bib \
    --csl=etc/apa.csl \
    $(INPUTS) \
    $(1)
endef

docx: $(DOCX)
$(DOCX): $(INPUTS) etc/smartnova18.docx
	$(call pandoc, --reference-doc=etc/smartnova18.docx --output $@)

html: $(HTML)
$(HTML): $(INPUTS)
	$(call pandoc, --standalone --mathjax --css etc/page.css --output $@)

echohtml:
	@echo $(HTML)

clean:
	rm -f $(DOCX) $(HTML)
