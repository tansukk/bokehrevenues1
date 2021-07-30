from numpy.lib.stride_tricks import DummyArray
import pandas
from bokeh.layouts import layout
from bokeh.models.glyphs import Circle
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import curdoc, show
from numpy import source
import pandas
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, Band, Toggle
from bokeh.models.annotations import Label, LabelSet, Span, BoxAnnotation
from bokeh.models.widgets import Select, Slider, RadioButtonGroup
from bokeh.layouts import gridplot
from bokeh.transform import dodge

data = pandas.read_csv("DATA/DATA.csv", sep=",")

data = data.dropna()

#print(data.columns)

data["TOTAL COLLECTED AMOUNT PERC"] = data["TOTAL COLLECTED AMOUNT"] / data["TOTAL CURRENT REV"]
data["TOTAL COLLECTED AMOUNT PERC"] = (data["TOTAL COLLECTED AMOUNT PERC"]).round(decimals=2)
#print(data["TOTAL COLLECTED AMOUNT PERC"])


data["SizeFor_Susp_Collect"] = data["SUSPICIOUS COLLECTIBLES OF ALL SALES"]*400
source = ColumnDataSource(data)

f = figure(x_range=data["REGION"])
f.vbar(x=dodge("REGION",-0.30, range=f.x_range), top="PREVIOUS CYCLE TOTAL SALES REVENUES", 
color="orangered", fill_alpha=.5,  width=.1, source=source, legend_label="Former Sales Cycle Total Revenues")
f.vbar(x=dodge("REGION",-0.20, range=f.x_range), top="TOTAL CURRENT REV", 
color="gold", fill_alpha=.6,  width=.1, source=source, legend_label="Current Total Sales Rev.")
f.vbar(x=dodge("REGION", 0, range=f.x_range), top="SALES REV ECO", 
color="darkblue", fill_alpha=.6,  width=.2, source=source, legend_label="Current Eco Prod. Sales Rev.")
f.vbar(x=dodge("REGION",-0.05, range=f.x_range), top="SALES REV PREMIUM", 
color="lightgreen", fill_alpha=.6,  width=.2, source=source, legend_label="Current Premium Prod. Sales Rev.")
f.vbar(x=dodge("REGION",-0.20, range=f.x_range), top="TOTAL COLLECTED AMOUNT", 
color="green", fill_alpha=.6,  width=.1, source=source, legend_label="Total Of Collected Amounts in Current Period")
f.circle(x="REGION", y=9000, size="SizeFor_Susp_Collect", 
color="red", fill_alpha=.5, legend_label="Ratio of Suspicious Collectibles", source=source)


Labels1 = LabelSet(x="REGION" ,y="TOTAL COLLECTED AMOUNT" ,text="TOTAL COLLECTED AMOUNT PERC", 
x_offset=-34, y_offset=0, text_font_size="6pt", text_color="white", background_fill_color= "darkgreen", text_alpha=0, background_fill_alpha=0, source=source)
f.add_layout(Labels1)
Labels2 = LabelSet(x="REGION" ,y="TOTAL CURRENT REV" ,text="TOTAL CURRENT REV", x_offset=-30, y_offset=0, text_font_size="6pt", text_alpha=0, background_fill_alpha=0, source=source)
f.add_layout(Labels2)
Labels3 = LabelSet(x="REGION" ,y="PREVIOUS CYCLE TOTAL SALES REVENUES" ,text="PREVIOUS CYCLE TOTAL SALES REVENUES", 
x_offset=-60, y_offset=-3, text_font_size="6pt", text_color="white", background_fill_color= "darkred", text_alpha=0, background_fill_alpha=0, source=source)
f.add_layout(Labels3)
Labels4 = LabelSet(x="REGION" ,y="SALES REV ECO" ,text="SALES REV ECO", 
x_offset=-2, y_offset=-3, text_font_size="6pt", text_color="white", background_fill_color= "darkblue", text_alpha=0, background_fill_alpha=0, source=source)
f.add_layout(Labels4)
Labels5 = LabelSet(x="REGION" ,y="SALES REV PREMIUM" ,text="SALES REV PREMIUM", 
x_offset=-3, y_offset=-3, text_font_size="6pt", text_color="white", background_fill_color= "darkgreen", text_alpha=0, background_fill_alpha=0, source=source)
f.add_layout(Labels5)
Labels6 = LabelSet(x="REGION", y=8200, text="SUSPICIOUS COLLECTIBLES OF ALL SALES", 
x_offset=0, y_offset=-10, text_font_size="10pt", text_color="white", background_fill_color= "red", text_alpha=0, 
background_fill_alpha=0, source=source)
f.add_layout(Labels6)


f.legend.background_fill_alpha = 0.1
f.legend.margin = 2
f.legend.padding = 2
f.legend.click_policy="hide"
f.legend.location = 'top_left'
f.legend.orientation = "horizontal"
f.legend.label_text_font_size = "7pt"

f.y_range = Range1d(start=0, end=10000)
f.plot_width = 1200
f.plot_height = 500

show_average_decision = 0
def show_values(arg):
    global show_average_decision
    show_average_decision = show_average_decision +1
    Labels1.text_alpha = (show_average_decision%2)
    Labels1.background_fill_alpha = (show_average_decision%2)
    Labels2.text_alpha = (show_average_decision%2)
    Labels2.background_fill_alpha = (show_average_decision%2)
    Labels3.text_alpha = (show_average_decision%2)
    Labels3.background_fill_alpha = (show_average_decision%2)
    Labels4.text_alpha = (show_average_decision%2)
    Labels4.background_fill_alpha = (show_average_decision%2)
    Labels5.text_alpha = (show_average_decision%2)
    Labels5.background_fill_alpha = (show_average_decision%2)
    Labels6.text_alpha = (show_average_decision%2)
    Labels6.background_fill_alpha = (show_average_decision%2)
toggle1 = Toggle(label="Show/Hide values", button_type="success", active=True)
toggle1.on_click(show_values)

lay_out2 = layout([[toggle1]])
plot_layout = gridplot([[f]],plot_width=1100, plot_height=500)

curdoc().add_root(plot_layout)
curdoc().add_root(lay_out2)



#show(f)

