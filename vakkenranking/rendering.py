from datetime import date
from jinja2 import Environment, PackageLoader
import pandas as pd
import csv


class CSVRenderer(object):

    def render(self, courses):
        courselist = [{**course, **{'code': code}} for code, course in courses.items()]
        sortedcourses = sorted(
            courselist,
            key=lambda x: (x['stats']['course']['mean'], x['stats']['course']['n']),
            reverse=True
        )

        f = lambda x: "{0:.2f}".format(x)
        fn = lambda x: int(x)
        df = pd.DataFrame({
            'code': [str(c['code']) for c in sortedcourses],
            'mean': [f(c['stats']['course']['mean']) for c in sortedcourses],
            'std': [f(c['stats']['course']['std']) for c in sortedcourses],
            'n': [fn(c['stats']['course']['n']) for c in sortedcourses],
            'teachers_mean': [f(c['stats']['teachers']['mean']) for c in sortedcourses],
            'teachers_std': [f(c['stats']['teachers']['std']) for c in sortedcourses],
            'teachers_n': [fn(c['stats']['teachers']['n']) for c in sortedcourses],
            'old_mean': [f(c['old_stats']['course']['mean']) if 'old_stats' in c else '' for c in sortedcourses],
            'old_std': [f(c['old_stats']['course']['std']) if 'old_stats' in c else '' for c in sortedcourses],
            'old_n': [fn(c['old_stats']['course']['n']) if 'old_stats' in c else '' for c in sortedcourses],
        })

        csv_str = df.to_csv(None,
            columns=['code', 'mean', 'std', 'n',
                     'teachers_mean', 'teachers_std', 'teachers_n',
                     'old_mean', 'old_std', 'old_n'],
            index=False,
            header=False,
            quoting=csv.QUOTE_ALL
        )

        return csv_str


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
