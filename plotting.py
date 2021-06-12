from motionDetect import df

from bokeh.plotting import figure,output_file,show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)



f=figure(x_axis_type="datetime",height=100,width=500,title="Motion Graph",sizing_mode="scale_width")
f.yaxis.minor_tick_line_color=None

#f.ygrid[0].ticker.desired_num_ticks=1
q=f.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
f.add_tools(hover)
print(df["Start_string"][0])
print(df["End_string"][0])
output_file("7. Webcam\\Graph.html")
show(f)