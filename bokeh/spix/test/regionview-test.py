#!/usr/bin/env bokeh serve --show

from bokeh.plotting import curdoc
from regionview import UN_regions, RegionView

curdoc().add_root(RegionView(UN_regions()).model())
