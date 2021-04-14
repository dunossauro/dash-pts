

def velocity(sprints_data):
    return {
        'data': [
            {  # commitment
                'x': sprints_data['names'],
                'y': sprints_data['commitment'],
                'type': 'bar',
                'line': {'color': 'gren', 'width': 3},
            },
            {  # completed
                'x': sprints_data['names'],
                'y': sprints_data['completed'],
                'type': 'bar',
                'line': {'color': 'red', 'width': 3},
            },
        ],
        'layout': {
            'title': {
                'text': 'Velocity',
                'x': 0.05,
                'xanchor': 'left',
            }
        }
    }
