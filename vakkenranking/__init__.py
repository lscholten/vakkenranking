__author__ = 'Luuk Scholten'
__email__ = 'info@luukscholten.com'
__version__ = '0.0.1'


def run(argv=None):
    """Vakkenranking
    Usage:
     vakkenranking [--output=<type>]
     vakkenranking (-h | --help)

    -h --help           show this
    --output=<type>     {html, csv} [default: html]
    """
    import sys
    from docopt import docopt
    from vakkenranking.parsing import Parser
    from vakkenranking.mapping import Mapper
    from vakkenranking.statistics import StatsCalculator
    from vakkenranking.rendering import CSVRenderer, HtmlRenderer

    # Check for the version
    if not sys.version_info >= (3, 5):
        print('This python version is not supported. Please use python 3.4')
        exit(1)

    argv = argv or sys.argv[1:]
    docblock = run.__doc__
    arguments = docopt(docblock, argv)

    if arguments['--output'] not in ['html', 'csv']:
        print("Invalid argument, expected --output=html or --output=csv")
        exit(1)

    parser = Parser()
    old = parser.parse('data/old')
    new = parser.parse('data/new')

    sc = StatsCalculator()
    old = sc.calculate(old)
    new = sc.calculate(new)

    mapper = Mapper()
    courses = mapper.map_courses(new, old)

    if arguments['--output'] == 'html':
        renderer = HtmlRenderer()
    else:
        renderer = CSVRenderer()

    print(renderer.render(courses))
