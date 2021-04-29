import json
import pygal
import datetime
import dateutil.parser as dateparser

# 1. Line Graph
# - Measuring the motivational results
# - X-axis => time spent of user
# - Y-axis => scores made by usercle

# 2. Bar Graph
# - Comparing User’s scores
# - X-axis => Username
# - Y-axis => Score

# 3. Pie Chart
# - Measuring the time spent on each level
# The pie chart will contain an average of times that take stage user to complete a level


def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    return data

def get_user_data(filename, username):
    data = load_data(filename)
    for userdata in data:
        if userdata["username"] == username:
            return userdata
    return None

def get_diff_in_secs(start, end):
    start = dateparser.isoparse(start)
    end = dateparser.isoparse(end)
    difference = end - start
    seconds_in_day = 24 * 60 * 60
    m, s = divmod(difference.days * seconds_in_day + difference.seconds, 60)
    return m * 60 + s


def get_levels_percentages(userdata):
    levels = userdata["levels"]
    levels = [
        (
            f"Level {level['level']}",
            get_diff_in_secs(level["starttime"], level["endtime"]),
        )
        for level in levels
    ]
    total_time = sum([l[1] for l in levels])
    levels_data = [(l[0], l[1] / total_time * 100) for l in levels]
    return levels_data


def draw_pie_chart(username):
    pie_chart = pygal.Pie()
    pie_chart.title = "Time Spend on Each Level"
    userdata = get_user_data("./scores.json", "Name ")
    levels_data = get_levels_percentages(userdata)
    for piece in levels_data:
        title, percent = piece
        pie_chart.add(title, percent)
    pie_chart.render_to_file("./out/piechart.svg")


def draw_bar_graph():
    pass


def draw_line_graph():
    pass


def create_graph_data():
    pass


draw_pie_chart("Google")
