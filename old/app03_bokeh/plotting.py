from bokeh.plotting import figure, output_file, show
from motion_detector import df

p=figure(x_axis_type='datetime', height=100, width=500, title='Motion graph')
p.yaxis.minor_tick_line_color=None
#p.ygrid[0].ticker.desired_num_ticks=1

q=p.quad(left=df['Start'],right=df['End'],bottom=0,top=1,color='green')

output_file('Graph1.html')
show(p)