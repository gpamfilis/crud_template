import pandas as pd
# https://bokeh.pydata.org/en/latest/docs/user_guide/categorical.html#visual-dodge
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, LabelSet
# from bokeh.palettes import Spectral6,
from bokeh.plotting import figure


def vertical_bar_chart_from_data_frame(data_frame, category_name, column_to_plot='AMOUNT'):
    data_frame.index = pd.to_datetime(data_frame.index)
    prep = data_frame[data_frame.outflows == category_name]
    cat = prep.groupby(pd.Grouper(freq='M')).sum()[column_to_plot]
    dates = cat.index.strftime("%Y-%m-%d").tolist()
    counts = cat.tolist()
    source = ColumnDataSource(data=dict(fruits=dates, counts=counts))  # , color=Spectral6

    p = figure(x_range=dates, y_range=(0, 1.6 * max(counts)), title=category_name,
               toolbar_location=None, tools="", width=400, height=400)
    p.vbar(x='fruits', top='counts', width=0.9, source=source)  # , color='color' legend="fruits",
    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    p.xaxis.major_label_orientation = 3.14 / 2
    return p


import numpy as np


def vertical_bar_chart_from_data_frame2(data_frame, column='AMOUNT', title='test'):
    m = data_frame[column].values.astype(float)
    print(data_frame)
    dates = data_frame.index.values.tolist()
    counts = m.tolist()
    print(dates, counts)
    source = ColumnDataSource(
        data=dict(fruits=dates, counts=counts))  # , color=Spectral6
    p = figure(x_range=dates, y_range=(0, 1.6 * max(m)), title=title,
               toolbar_location='right', tools="save", width=400, height=300,responsive = True)
    
    p.vbar(x='fruits', top='counts', width=0.9, source=source)  # , color='color'

    p.xaxis.axis_label="Table Columns"
    p.xaxis.axis_label_text_font_size = "25pt"
    p.xaxis.major_label_text_font_size = "25pt"
    p.xaxis.axis_label_text_font = "times"
    p.xaxis.axis_label_text_color = "black"

    p.yaxis.axis_label="Percentage"
    p.yaxis.axis_label_text_font_size = "25pt"
    p.yaxis.major_label_text_font_size = "25pt"
    p.yaxis.axis_label_text_font = "times"
    p.yaxis.axis_label_text_color = "black"

    labels = LabelSet(x='fruits', y='counts', text='counts', level='glyph',
                      x_offset=0, y_offset=0, source=source, render_mode='canvas', angle=45)

    # plot.vbar(source=source, x='x', top='y', bottom=0, width=0.3, color=PuBu[7][2])

    p.add_layout(labels)
    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    p.xaxis.major_label_orientation = 3.14 / 2
    return p
