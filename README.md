FFilter
=======

FFilter - tool for screening open data for private/sensitive information before publication

This prototype is developed as part of Random Hacks of Kindness, Washington, DC - June 2-3, 2012

Here is problem statement - http://www.rhok.org/problems/ffilter-tool-screening-open-data-privatesensitive-information-publication

Features
--------

- supports Excel 2007 file format only

- scans all the data in spreadsheet for sensitive information (e.g. SSNs)

- simple command line tool

Requirements
------------

Python 2.7
OpenPyXL library - http://packages.python.org/openpyxl/

Usage
-----

python ffilter.py Sample.xlsx