all: docx

MARKDOWN=vsj18.md md/*.md
DOCX=vsj18-wakita.docx
HTML=vsj18-wakita.html

define pandoc
  pandoc \
    --bibliography=library.bib \
    --filter pandoc-citeproc \
    --csl=etc/apa.csl \
    --standalone \
    $(1) \
    $(MARKDOWN)
endef

docx: $(DOCX)
$(DOCX): $(MARKDOWN) etc/smartnova18.docx
	$(call pandoc, --reference-doc=etc/smartnova18.docx --output $@)

html: $(HTML)
$(HTML): $(MARKDOWN)
	@$(call pandoc, --css etc/page.css --self-contained --output $@)

echohtml:
	@echo $(HTML)

clean:
	rm -f $(DOCX) $(HTML)
