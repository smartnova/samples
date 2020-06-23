import numpy as np
from bokeh.plotting import figure, output_notebook, show
from bokeh.models import HoverTool, ColumnDataSource, CustomJS

JS_CODE = '''
    if (cb_data.renderer.id==r.id) {
      sds.selected.indices = cb_data.index.indices;
    }'''

# HoverTool:htがrenderer:r 上でhoverしたdatasource上のindiceに対してcallbackする

def add_python_hover_callback(hover_tool, r, callback):
    ds_for_get_selected = ColumnDataSource(dict(_=[None]*len(r.data_source.data)))
    js_callback = CustomJS(args={'sds': ds_for_get_selected, 'r':r}, code=JS_CODE)

    ds_for_get_selected.selected.on_change('indices', callback)
    #hover_tool.callback = js_callback if hover_tool.callback is None else hover_tool.callback + [js_callback]
    hover_tool.callback = (hover_tool.callback or []) + [js_callback]

def Document(doc):
    p = figure()

    # r1についてcallback
    ds_blue = ColumnDataSource(dict(x=np.random.rand(5), y=np.random.rand(5), c=['blue']*5))
    blues = p.circle(x='x', y='y', fill_color='c', line_color='c', source=ds1)

    # r2についてはcallbackしない
    ds_red = ColumnDataSource(dict(x=np.random.rand(5), y=np.random.rand(5), c=['red']*5))
    reds = p.circle(x='x', y='y', fill_color='c', line_color='c', source=ds2)

    # callbackの用意

    def callback_for_reds(attr, old, new):
        print(attr, old, new)
        print(ds_blue.data['x'][new])

    hover_tool = HoverTool()
    add_python_hover_callback(hover_tool, reds, callback_for_reds)

    p.add_tools(hover_tool)
    doc.add_root(p)

show(mod_doc)

# output_notebook()
# show(Document, notebook_url='localhost:8889')
