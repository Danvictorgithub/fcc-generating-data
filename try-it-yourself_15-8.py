from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()
results = []
num_rolls = 10000
for roll_num in range(num_rolls):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result +1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(
    title=f'Results of rolling two D6 {num_rolls} times but the results are multiplied',
    xaxis=x_axis_config,
    yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')