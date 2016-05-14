from datetime import date
from jinja2 import Environment, PackageLoader


class CSVRenderer(object):

    def render(self, courses):
        return "Not yet implemented!"


class HtmlRenderer(object):

    def render(self, courses):
        env = Environment(loader=PackageLoader('vakkenranking','templates'))
        template = env.get_template('template.html')

        courselist = [{**course, **{'code': code}} for code, course in courses.items()]
        sortedcourses = sorted(
            courselist,
            key=lambda x: (x['stats']['course']['mean'], x['stats']['course']['n']),
            reverse=True
        )

        if date.today().month >= 9:
            year = date.today().year
        else:
            year = date.today().year - 1

        return template.render(courses=sortedcourses, year=year)
