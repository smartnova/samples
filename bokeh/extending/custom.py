from bokeh.core.properties import String, Instance
from bokeh.models import HTMLBox, Slider

class Custom(HTMLBox):
    __implementation__ = 'custom.ts'
    text = String(default='Custom Text')
    slider = Instance(Slider)

from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import Slider

slider = Slider(start=0, end=10, step=0.1, value=0, title='value')
custom = Custom(text='Special Slider Display', slider=slider)
layout = column(slider, custom)
show(layout)
