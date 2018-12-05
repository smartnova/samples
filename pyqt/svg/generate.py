#!/usr/bin/env python

# svgwrite Documentation: https://svgwrite.readthedocs.io/en/master/

import svgwrite as svg

g = svg.Drawing('sample.svg', profile='tiny')
g.add(g.line((0, 10), (100, 10), stroke=svg.rgb(20, 20, 80, '%')))
g.add(g.text('Testing', insert=(0, 23), fill='red'))
g.add(g.polyline([(0, 30), (10, 40), (20, 30), (30, 40), (40, 30), (30, 40)], stroke=svg.rgb(0, 30, 0, '%'), fill='none'))
g.add(g.rect((0, 50), (100, 10), fill=svg.rgb(80, 20, 20, '%')))
p = g.path(d=('m', 0, 70), stroke='red', fill='none', stroke_width=0.02)
p.push('q', 5,-10, 10,0); p.push('q', 5,10, 10,0)
p.push('q', 5,-10, 10,0); p.push('q', 5,10, 10,0)
p.push('q', 5,-10, 10,0); p.push('q', 5,10, 10,0)
p.push('q', 5,-10, 10,0); p.push('q', 5,10, 10,0)
g.add(p)
g.save()

from viewer import SVG
SVG('sample.svg')
