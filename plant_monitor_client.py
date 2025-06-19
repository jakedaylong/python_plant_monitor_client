#pylint: disable=line-too-long
"""This example shows how to create a dashboard with multiple gauges"""
from nicegui import ui, app
import radio_data as rd
import db_conn

cursor = db_conn.init_conn()   

planter_data = rd.read_data()

db_conn.push_data(cursor, planter_data) 

planterA = {
'id': 1,
'name': 'Planter A',
'wetness': planter_data['wetness'],
'temperature': planter_data['humidity'],
'humidity': planter_data['temp'] * 1.8 + 32}

rows = [
    {'id': planterA['id'], 'name': planterA['name'], 'wetness': planterA['wetness'], 'temperature': planterA['temperature'], 'humidity': planterA['humidity']}]

columns = [
        {'id': 'id', 'label': 'ID', 'field': 'id'},
        {'id': 'name', 'label': 'Name', 'field': 'name'},
        {'id': 'wetness', 'label': 'Wetness', 'field': 'wetness', 'sortable' : True},
        {'id': 'temperature', 'label': 'Temperature', 'field': 'temperature'},
        {'id': 'humidity', 'label': 'Humidity', 'field': 'humidity'}]

plant_table = ui.table(
            columns=columns,
            rows=rows,
            row_key='id',
            title='Plant Data')

ui.separator()
ui.label(planterA['name']+':').classes('text-2xl font-bold text-center')

# Create a row of gauges for each planter for soil wetness
# The row is created using a for loop that iterates over the list of planters
with ui.row():
    for planter in [planterA]:
        # Set the color of the gauge based on the wetness value
        # The color is set to green if the wetness is above 60, orange if it is above 30, and red if it is below 30
        wetness_chart = ui.highchart({
            'chart': {
                'type': 'gauge',
                'plotBackgroundColor': None,
                'plotBackgroundImage': None,
                'height': 350,
                'width': 350,
            },

            'title': {
                'text': planter['name'] + ' Wetness',
                'floating': True,
            },

            'pane': {
                'startAngle': -90,
                'endAngle': 89.9,
                'background': None,
                'center': ['50%', '75%'],
                'size': '90%'
            },

            'yAxis': {
                'min': 0,
                'max': 100,
                'tickPixelInterval': 72,
                'tickPosition': 'inside',
                'tickColor': '#FFFFFF',
                'tickLength': 20,
                'tickWidth': 2,
                'minorTickInterval': 'null',
                'labels': {
                    'distance': 20,
                    'style': {
                        'fontSize': '14px'
                    }
                },
                'lineWidth': 0,
                'plotBands': [{
                    'from': 0,
                    'to': 30,
                    'color': 'red',
                    'thickness': 20,
                    'borderRadius': '50%'
                }, {
                    'from': 31,
                    'to': 59,
                    'color': 'orange',
                    'thickness': 20,
                    'borderRadius': '50%'
                }, {
                    'from': 60,
                    'to': 100,
                    'color': 'green',
                    'thickness': 20,
                    'borderRadius': '50%'
                }]
            },
            'series': [{
                'name': 'Wetness',
                'data': [planter['wetness']],
                'tooltip': {
                    'valueSuffix': '%'
                },
                'dataLabels': {
                    'format': '{y} %',
                    'borderWidth': 0,
                    'color': '#333333',
                    'style': {
                        'fontSize': '16px'
                    }
                },
            'dial': {
                'radius': '80%',
                'backgroundColor': 'gray',
                'baseWidth': 12,
                'baseLength': '0%',
                'rearLength': '0%'
            },
            'pivot': {
                'backgroundColor': 'gray',
                'radius': 6
            }

    }]
            })
        temp_chart = ui.highchart({
            'chart': {
                'type': 'gauge',
                'plotBackgroundColor': None,
                'plotBackgroundImage': None,
                'height': 350,
                'width': 350,
            },

            'title': {
                'text': planter['name'] + ' Temperature',
                'floating': True,
            },

            'pane': {
                'startAngle': -90,
                'endAngle': 89.9,
                'background': None,
                'center': ['50%', '75%'],
                'size': '90%'
            },

            'yAxis': {
                'min': 0,
                'max': 100,
                'tickPixelInterval': 72,
                'tickPosition': 'inside',
                'tickColor': '#FFFFFF',
                'tickLength': 20,
                'tickWidth': 2,
                'minorTickInterval': 'null',
                'labels': {
                    'distance': 20,
                    'style': {
                        'fontSize': '14px'
                    }
                },
                'lineWidth': 0,
                'plotBands': [{
                    'from': 0,
                    'to': 32,
                    'color': 'blue',
                    'thickness': 20,
                    'borderRadius': '50%'
                }, {
                    'from': 33,
                    'to': 45,
                    'color': 'red',
                    'thickness': 20,
                    'borderRadius': '50%'
                }, {
                    'from': 46,
                    'to': 75,
                    'color': 'green',
                    'thickness': 20,
                    'borderRadius': '50%'
                },
                {
                    'from': 76,
                    'to': 100,
                    'color': 'orange',
                    'thickness': 20,
                    'borderRadius': '50%'
                }]
            },
            'series': [{
                'name': 'Temperature',
                'data': [planter['temperature']],
                'tooltip': {
                    'valueSuffix': 'F'
                },
                'dataLabels': {
                    'format': '{y:.2f}F',
                    'borderWidth': 0,
                    'color': '#333333',
                    'style': {
                        'fontSize': '16px'
                    }
                },
            'dial': {
                'radius': '80%',
                'backgroundColor': 'gray',
                'baseWidth': 12,
                'baseLength': '0%',
                'rearLength': '0%'
            },
            'pivot': {
                'backgroundColor': 'gray',
                'radius': 6
            }

    }]
            })
        humidity_chart = ui.highchart({
            'chart': {
                'type': 'gauge',
                'plotBackgroundColor': None,
                'plotBackgroundImage': None,
                'height': 350,
                'width': 350,
            },

            'title': {
                'text': planter['name'] + ' Humidity',
                'floating': True,
            },

            'pane': {
                'startAngle': -90,
                'endAngle': 89.9,
                'background': None,
                'center': ['50%', '75%'],
                'size': '90%'
            },

            'yAxis': {
                'min': 0,
                'max': 100,
                'tickPixelInterval': 72,
                'tickPosition': 'inside',
                'tickColor': '#FFFFFF',
                'tickLength': 20,
                'tickWidth': 2,
                'minorTickInterval': 'null',
                'labels': {
                    'distance': 20,
                    'style': {
                        'fontSize': '14px'
                    }
                },
                'lineWidth': 0,
                'plotBands': [{
                    'from': 0,
                    'to': 19,
                    'color': 'orange',
                    'thickness': 20,
                    'borderRadius': '50%'
                },{
                    'from': 20,
                    'to': 39,
                    'color': 'yellow',
                    'thickness': 20,
                    'borderRadius': '50%'
                }, {
                    'from': 40,
                    'to': 70,
                    'color': 'green',
                    'thickness': 20,
                    'borderRadius': '50%'
                }, {
                    'from': 71,
                    'to': 100,
                    'color': 'orange',
                    'thickness': 20,
                    'borderRadius': '50%'
                },]
            },
            'series': [{
                'name': 'Humidity',
                'data': [planter['humidity']],
                'tooltip': {
                    'valueSuffix': '%'
                },
                'dataLabels': {
                    'format': '{y} %',
                    'borderWidth': 0,
                    'color': '#333333',
                    'style': {
                        'fontSize': '16px'
                    }
                },
            'dial': {
                'radius': '80%',
                'backgroundColor': 'gray',
                'baseWidth': 12,
                'baseLength': '0%',
                'rearLength': '0%'
            },
            'pivot': {
                'backgroundColor': 'gray',
                'radius': 6
            }

    }]
            })

ui.separator()

def update_table():
    global planter_data
    planter_data = rd.read_data()

    global planterA
    planterA = {
    'id': 1,
    'name': 'Planter A',
    'wetness': planter_data['wetness'],
    'temperature': planter_data['temp'] * 1.8 + 32,
    'humidity': planter_data['humidity']}

    rows[0]['wetness'] = planterA['wetness']
    rows[0]['temperature'] = planterA['temperature']
    rows[0]['humidity'] = planterA['humidity']
    plant_table.update()

    humidity_chart.options['series'][0]['data'][0] = planterA['humidity']
    humidity_chart.update()
    
    temp_chart.options['series'][0]['data'][0] = planterA['temperature']
    temp_chart.update()
    
    wetness_chart.options['series'][0]['data'][0] = planterA['wetness']
    wetness_chart.update()

    db_conn.push_data(cursor, planter_data)


app.timer(5, update_table)
ui.run()




