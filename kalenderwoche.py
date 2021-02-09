#!/usr/bin/env python3
"""
kalenderwoche

Usage:
    kalenderwoche
    kalenderwoche --date <date>
    kalenderwoche -h|--help
Options:
    <date> An optional date (e.g. 2021-01-01)
    -h --help  Show this screen.
"""
import datetime
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)
    datum = datetime.datetime.now()
    if arguments['--date']:
        datum = datetime.datetime.strptime(arguments['<date>'], '%Y-%m-%d')
    kalenderwoche = datum.isocalendar()[1]

    print(f'{datum.strftime("%d.%m")} liegt in Kalenderwoche {kalenderwoche} im Jahr {datum.strftime("%Y")}')
