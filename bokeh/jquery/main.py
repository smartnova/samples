import json

from bokeh.plotting import curdoc
from bokeh.models import *

doc = curdoc()
doc.title = 'Bokeh-jQuery integration'

conversation = [{'utterer': f'Speaker {i%3}', 'utterance': f'Utterance #{i}'} for i in range(100)]
utterances = conversation[0:10]
WINDOW_SIZE = 5

print(json.dumps(utterances))

slider = Slider(start=0, end=len(conversation) - 10, value=0, step=1, title='Conversation window')
buffer = TextInput(name='buffer', value='[]', title='Buffer:')

def slider_on_change(attr, old, new):
    global utterances
    utterances = conversation[new:new+WINDOW_SIZE]
    buffer.value = json.dumps(utterances)
    print(utterances)
slider.on_change('value', slider_on_change)

js_buffer_on_change = CustomJS(args=dict(source=utterances), code="buffer_on_change();")
buffer.js_on_change('value', js_buffer_on_change)

view = Column(name='conversation',
              children=[slider, buffer],
              sizing_mode='scale_width')

doc.add_root(view)
