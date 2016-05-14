import numpy as np


class StatsCalculator(object):

    def _calculate_grade_statistics(self, grades):
        flatgrades = [grade for sublist in grades for grade in sublist]
        if len(flatgrades) > 0:
            return {
                'mean': np.mean(flatgrades),
                'std' : np.std(flatgrades),
                'n' : len(flatgrades) // len(grades),
            }

        return {'mean': 0, 'std': 0, 'n': 0}

    def calculate(self, courses):
        for k, v in courses.items():
            teacher_stats = self._calculate_grade_statistics(v['teacher_grades'])
            course_stats = self._calculate_grade_statistics(v['course_grades'])

            courses[k]['stats'] = {'teachers': teacher_stats, 'course': course_stats}
            courses[k].pop('teacher_grades')
            courses[k].pop('course_grades')

        return courses



