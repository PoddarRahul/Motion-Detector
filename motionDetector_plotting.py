from motionDetector import df
from bokeh.plotting import show,figure,output_file
from bokeh.models import HoverTool,ColumnDataSource

df["Start_str"]=df["Start"].dt.strftime("%d-%m-%Y %H:%M:%S")
df["End_str"]=df["End"].dt.strftime("%d-%m-%Y %H:%M:%S")
cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100,width=500,sizing_mode='scale_width',title='Motion Graph')
p.yaxis.minor_tick_line_color=None
# p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@Start_str"),("End","@End_str")])
p.add_tools(hover)

p.quad(left="Start",right="End",top=1,bottom=0,source=df)

output_file("MotionGraph.html")
show(p)
