from pendulum import datetime, period

from app.graphs.burn_down import auto_none_days, burn_down, guide


def test_auto_none_days_should_increment_all_list():
    points = []
    days = [1, 2, 3, 4, 5]
    assert [None, None, None, None, None] == auto_none_days(days, points)


def test_auto_none_days_should_increment_3_values():
    points = [
        1,
        2,
    ]
    days = [1, 2, 3, 4, 5]
    assert [1, 2, None, None, None] == auto_none_days(days, points)


def test_auto_none_days_shouldnt_increment():
    points = [1, 2, 3, 4, 5]
    days = [1, 2, 3, 4, 5]
    assert [1, 2, 3, 4, 5] == auto_none_days(days, points)


def test_guide_with_weekend():
    """
    day 1: 50 - start day
    day 2: 50 - weekend
    day 3: 50 - weekend
    day 4: 25 - weekday
    day 5: 00 - final day
    """
    total_points = 50
    graph_period = list(period(datetime(2021, 1, 1), datetime(2021, 1, 5)))
    assert [50, 50, 50, 25, 0] == guide(total_points, graph_period)


def test_guide_without_weekend():
    total_points = 50
    graph_period = list(period(datetime(2021, 1, 4), datetime(2021, 1, 8)))
    assert [50, 37.5, 25, 12.5, 0] == guide(total_points, graph_period)


def test_burn_down_graph_guide_values():
    graph_values = burn_down(
        sprint='',
        initial_data=datetime(2021, 1, 4),
        final_data=datetime(2021, 1, 8),
        total_points=50,
        sprint_data=[],
    )

    guide = graph_values['data'][0]
    assert guide['y'] == [50, 37.5, 25, 12.5, 0]


def test_burn_down_graph_sprint_values_in_start_of_sprint():
    graph_values = burn_down(
        sprint='',
        initial_data=datetime(2021, 1, 4),
        final_data=datetime(2021, 1, 8),
        total_points=50,
        sprint_data=[],
    )

    guide = graph_values['data'][1]
    assert guide['y'] == [None, None, None, None, None]


def test_burn_down_graph_sprint_values_in_middle_of_sprint():
    sprint_data = [1, 2, 3]

    graph_values = burn_down(
        sprint='',
        initial_data=datetime(2021, 1, 4),
        final_data=datetime(2021, 1, 8),
        total_points=50,
        sprint_data=sprint_data,
    )

    guide = graph_values['data'][1]
    assert guide['y'] == sprint_data + [None, None]


def test_burn_down_graph_sprint_values_in_end_of_sprint():
    sprint_data = [1, 2, 3, 4, 5]

    graph_values = burn_down(
        sprint='',
        initial_data=datetime(2021, 1, 4),
        final_data=datetime(2021, 1, 8),
        total_points=50,
        sprint_data=sprint_data,
    )

    guide = graph_values['data'][1]
    assert guide['y'] == sprint_data


def test_burn_down_graph_period():
    graph_period = period(datetime(2021, 1, 4), datetime(2021, 1, 8))
    graph_values = burn_down(
        sprint='',
        initial_data=datetime(2021, 1, 4),
        final_data=datetime(2021, 1, 8),
        total_points=50,
        sprint_data=[],
    )

    guide = graph_values['data'][0]
    assert guide['x'] == list(graph_period)
