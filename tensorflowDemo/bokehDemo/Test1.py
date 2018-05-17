# coding:utf-8
from bokeh.plotting import figure, output_file,show


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    output_file('lines.html', title='line plot example')
    p = figure(title='simple line example',x_axis_label='x', y_axis_label='y')
    p.line(x, y, legend='Line A.', line_width=2)
    show(p)






