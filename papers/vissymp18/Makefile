all: docx

HEADER=vsj18-header.md
MACRO=macros.sty
MARKDOWN=md/*.md
INPUTS=$(HEADER) $(MACRO) $(MARKDOWN)

DOCX=vsj18-wakita.docx
HTML=vsj18-wakita.html

define pandoc
  pandoc \
    --from markdown+latex_macros \
    --filter pandoc-citeproc \
    --bibliography=library.bib \
    $(INPUTS) \
    $(1)
endef
#    引用の形式を Chicogo 形式でなく APA 形式に変更する場合は以下の行を指定する。
#    --csl=etc/apa.csl \

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
