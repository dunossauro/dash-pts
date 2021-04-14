from operator import getitem

from pendulum import period


def auto_none_days(days, points):
    """Autoincrement don't works days yet with None."""
    return points + [None for _ in range(len(days) - len(points))]


def guide(total_points, graph_period):
    """Gerenate guide line with dayoffs."""

    def weekday(day):
        return not day.weekday() in (5, 6)

    days = [(day, weekday(day)) for day in graph_period]
    n_days = len(list(filter(lambda x: getitem(x, 1), days)))

    median_points = total_points / (n_days - 1)
    last_value = total_points
    out = []

    for n, (date, valid) in enumerate(days):
        if valid and n != 0:
            last_value = last_value - median_points
            out.append(last_value)
        else:
            out.append(last_value)

    return out


def burn_down(sprint, initial_data, final_data, total_points, sprint_data):
    graph_period = list(period(initial_data, final_data).range('days'))

    y = auto_none_days(graph_period, sprint_data)

    return {
        'data': [
            {  # Guide
                'x': graph_period,
                'y': guide(total_points, graph_period),
                'name': 'Guides',
                'type': 'scatter',
                'mode': 'lines',
                'line': {'color': 'grey', 'width': 3},
            },
            {  # Sprint_data
                'x': graph_period,
                'y': y,
                'type': 'scatter',
                'name': 'Points',
                'line': {'color': 'red', 'width': 3},
            },
        ],
        'layout': {
            'title': {
                'text': 'Burn Down',
                'x': 0.05,
                'xanchor': 'left',
            }
        }
    }
