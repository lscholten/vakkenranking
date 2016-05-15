import os


class Mapper(object):

    def __init__(self, mapping_file='mapping.csv'):
        if not os.path.exists(mapping_file):
            print('Mapping file missing, cannot continue.')
            exit(1)

        with open(mapping_file, 'r') as mapping:
            self.mapping = { kv[0]:kv[1] for kv in (line.strip().split(",") for line in mapping.readlines()) }

    def map_courses(self, new, old):
        for code, stats in new.items():
            new[code]['is_new'] = False
            if code in old:
                new[code]['old_stats'] = old[code]['stats']
            elif code in self.mapping.keys() and self.mapping[code] == 'new':
                new[code]['is_new'] = True
            elif code in self.mapping.keys():
                new[code]['old_stats'] = old[self.mapping[code]]['stats']

        return new