import pandas as pd
import numpy as np
import re
import os
import sys


class Parser(object):

    _filename_rule = ".*_(?:NWI-)?([^\\_^-]+)_(.+)_([0-9]+)_(.+)\\.xls"

    _teachergrade_keys = [
        "I would rate the performance of the lecturer\\(s\\)/teacher\\(s\\) as \\[(.+)\\]",
        "Ik geef de docent\\(en\\) het volgende cijfer \\[(.+)\\]",
    ]

    _coursegrade_keys = [
        "[Ik geef deze cursus het volgende rapportcijfer] Ik geef deze cursus het volgende rapportcijfer",
        "Ik geef deze cursus het volgende rapportcijfer [Ik geef deze cursus het volgende rapportcijfer]",
        "[I would rate this course] On a scale from 1 to 10 (10 being excellent) I would rate this course",
        "On a scale from 1 to 10 (10 being excellent) I would rate this course [I would rate this course]",
        "Rating [I would rate this course overall as]",
        "Cijfer [Ik geef deze cursus als geheel het volgende cijfer]",
    ]

    def _parse_filename(self, filename):
        match = re.match(self._filename_rule, filename)

        return {
            'code': match.groups()[0],
            'name': match.groups()[3],
            'course_grades': None,
            'teacher_grades': None,
        }

    def _parse_coursegrade(self, dataframe):
        df_keys = list(dataframe.keys())
        keys = [x for x in self._coursegrade_keys if x in df_keys]

        grades = [[x for x in dataframe[k] if not np.isnan(x)] for k in keys]
        return grades

    def _parse_teachergrades(self, dataframe):
        df_keys = list(dataframe.keys())
        keys = [x for x in df_keys for y in self._teachergrade_keys if re.match(y, x)]

        grades = [[x for x in dataframe[k] if not np.isnan(x)] for k in keys]
        return grades

    def parse(self, path):
        if not os.path.exists(path):
            print("Error: folder could not be read")
            exit(1)

        # Temporarily catch stdout to suppress xlrd warnings
        sysout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

        courses = {}

        for root, subdir, files in os.walk(path):
            xls = [x for x in files if x.endswith('xls')]
            for filename in xls:
                course = self._parse_filename(filename)
                df = pd.read_excel(os.path.join(root, filename), encoding='ISO-8859-1')
                course['course_grades'] = self._parse_coursegrade(df)
                course['teacher_grades'] = self._parse_teachergrades(df)

                courses[course['code']] = course

        sys.stdout = sysout
        return courses
