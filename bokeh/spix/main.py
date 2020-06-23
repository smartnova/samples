from bokeh.plotting import curdoc

from spix.regions import RegionMenus
from spix.indices import IndexMenus
#from spix.details import Details
from spix.map import Map

doc = curdoc()
doc.title = 'SPI Explorer'
RegionMenus(doc)
IndexMenus(doc)
Map(doc)
#Details(doc)

''' テンプレート変数の使い方。これらのフィールドは templates/index.html で利用できる。
tv = doc.template_variables
tv['foo'] = 'foo'
tv['bar'] = 5
tv['hoge'] = [1, dict(x='123')]
'''
