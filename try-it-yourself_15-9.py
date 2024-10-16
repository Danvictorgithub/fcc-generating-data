from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die(8)
die_2 = Die(8)

num_rolls = 1_000_000
results = [die_1.roll() + die_2.roll() for _ in range(num_rolls)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_result+1)]

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(
    title=f'Results of rolling two D8 {num_rolls} times',
    xaxis=x_axis_config,
    yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')