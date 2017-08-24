# sources/selected-crimes-local-authorities-2012-2015-*

Collection of data about Israeli Police events by local authorities and collection of selected crimes.

Data source: https://www.odata.org.il/dataset/maazarim1

Contains data for years 2012-2015.

## Overview

Contains 4 XLS (see in sources directory), files are identified by their suffix:

* 1b-small
* 2a-large
* 2a-small
* 2b-large

Some of these files have multiple sheets.

Not all sheets are processed, see the commented-out sheets in plus_plus.source-spec.yaml

The final data is normalized to a single table with `resource` column identifying the source XLS file / sheet number.

As of time of writing, these are the XLS files and sheets available:

![](https://github.com/OriHoch/israel-crime-data/raw/master/selected-crimes-local-authorities-2012-2015/.README_images/sheets_overview.png)

So really we are left with only 1 sheet which is worth investigating further:

## resource: 2a-large-sheet-2

Offences are grouped by major stat_group and specific offences:

![](https://github.com/OriHoch/israel-crime-data/raw/master/selected-crimes-local-authorities-2012-2015/.README_images/stat_group_offence.png)

Place names and more specific region codes are available:

![](https://github.com/OriHoch/israel-crime-data/raw/master/selected-crimes-local-authorities-2012-2015/.README_images/place_name_code.png)

Each value is per year quarter:

![](https://github.com/OriHoch/israel-crime-data/raw/master/selected-crimes-local-authorities-2012-2015/.README_images/year_quarter.png)
