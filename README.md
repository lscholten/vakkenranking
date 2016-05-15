# vakkenranking
Parsing application for Radboud University evaluations, for use by the OLC Informatica & Informatiekunde.

## Installation instructions
`pip install vakkenranking`

## How to use
```
Usage:
     vakkenranking [--output=<type>] [--new-dir=<dir>] [--old-dir=<dir>] [--mapping-file=<file>]
     vakkenranking (-h | --help)

    -h --help               show this
    --output=<type>         {html, csv} [default: html]
    --old-dir=<dir>         directory for last years evaluations [default: old]
    --new-dir=<dir>         directory for current evaluations [default: new]
    --mapping-file=<file>   location of mapping file [default: mapping.csv]
```

The following files and directories are required:
* A mapping file (default `mapping.csv`), which maps new courses to old courses (in that order), or with the entry `new`.
Note: if you have nothing to map, you must still supply an empty mapping file.
```
IPC021,IBI002
IPC019,IPC012
IPC020,new
IBC018,new
```
* A directory (default `new`) containing the `xls` evaluations for the current semester or year.
  The evaluations can stay in their course-specific folders.
* A directory (default `old`) containing the same evaluations, but for the previous year.

The course codes from both years are matched and can currently not be overruled by the `mapping.csv` file.

The `mapping.csv` file can also be used for the `cloaca` project.

## Dependencies

`vakkenranking` can be used with `Python >= 3.5`.
Required Python packages are described in `requirements.txt`, these will be installed by pip.

## Acknowledgements
This program started as a Python port of [Wassasin/vakkenranking](https://github.com/Wassasin/vakkenranking).
