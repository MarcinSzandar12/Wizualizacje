import plotly.graph_objects as go

salaries = [
	("Mark", 1000),
	("John", 1500),
	("Daniel", 2300),
	("Greg", 5000)
]

names = list(map(lambda tup:tup[0], salaries))
salary_values = list(map(lambda tup:tup[1], salaries))

data = go.Bar(x=names, y=salary_values)
layout = {
	'title': 'Salaries with plotly'
}
fig = go.Figure(data, layout)
fig.show()
