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
