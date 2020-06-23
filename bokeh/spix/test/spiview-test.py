#!/usr/bin/env bokeh serve --show

from bokeh.plotting import curdoc
from spiview import spi_hierarchy, SPIView

curdoc().add_root(SPIView(spi_hierarchy()).model())
