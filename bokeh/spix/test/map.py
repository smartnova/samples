import numpy as np
import pandas as pd

SPI = Needs, Wellbeing, Opportunity = ['Basic Human Needs', 'Foundations of Wellbeing', 'Opportunity']
spi2019 = pd.read_excel('../data/spi2019.xlsx', sheet_name='2019')[['Country'] + SPI]
spi2019 = spi2019[spi2019['Country'] != 'World']

mean, std = spi2019.mean('rows'), spi2019.std('rows')
spi2019['Needs'], spi2019['Wellbeing'], spi2019['Opportunity'] = [
    ((spi2019[i] - mean[i]) / std[i] * 10 + 80).clip(50, 100)
    for i in SPI]
print(spi2019)

from colormath.color_objects import ColorBase, sRGBColor as sRGB, LabColor as Lab
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

# sRGB
sRGB.fromHex = lambda hex: sRGB.new_from_rgb_hex(hex)
sRGB.hex = lambda c: c.get_rgb_hex()
sRGB.clamp = lambda c: sRGB(*[c.clamped_rgb_r, c.clamped_rgb_g, c.clamped_rgb_b])
ColorBase.values = ColorBase.get_value_tuple

# 色変換
ColorBase.sRGB = lambda c: c if isinstance(c, sRGB) else convert_color(c, sRGB)
ColorBase.Lab  = lambda c: c if isinstance(c, Lab)  else convert_color(c, Lab)

# 色距離
ColorBase.delta = lambda c1, c2: delta_e_cie2000(c1.Lab(), c2.Lab())

labs = [np.array([50, 50 * np.cos(theta), 50 * np.sin(theta)])
        for theta in np.linspace(0, 2 * np.pi, num=4)[:-1]]

import geopandas as gpd
world = gpd.read_file('../data/world.geo.json/countries.geo.json')
