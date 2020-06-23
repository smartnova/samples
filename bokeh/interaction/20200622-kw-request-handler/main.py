#!/usr/bin/env python
# coding: utf-8

import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models import HoverTool, ColumnDataSource, CustomJS

JS_CODE = '''
    if (cb_data.renderer.id==glyph.id) {
      selection.selected.indices = cb_data.index.indices;
    }'''

def ask_js_callback_to_call(hover_tool, glyph, py_callback):
    selection = ColumnDataSource()
    selection.selected.on_change('indices', py_callback)

    # 選択された領域が更新されたときに JS コールバックを読む仕組み
    js_callback = CustomJS(args={'selection': selection, 'glyph': glyph}, code=JS_CODE)
    #hover_tool.callback = js_callback if hover_tool.callback is None else hover_tool.callback + [js_callback]
    hover_tool.callback = js_callback

def Document(doc):
    (B, R) = 5, 5

    fig = figure()
    blue_points = fig.circle(x='x', y='y', fill_color='blue', line_color=None,
                             source=ColumnDataSource(dict(x=np.random.rand(B), y=np.random.rand(B))))
    red_points = fig.circle(x='x', y='y', fill_color='red', line_color=None,
                            source=ColumnDataSource(dict(x=np.random.rand(R), y=np.random.rand(R))))

    def py_callback(action, _, i):
        if len(i) > 0:
            print(f'{action}({i[0]}) -> x={red_points.data_source.data["x"][i][0]:.3f}')

    hover_tool = HoverTool()
    ask_js_callback_to_call(hover_tool, red_points, py_callback)

    fig.add_tools(hover_tool)
    doc.add_root(fig)

doc = curdoc()
Document(doc)
