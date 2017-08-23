#!/usr/bin/env bash

# traffic
curl https://www.odata.org.il/dataset/36f85402-fed3-4386-9963-a5270abebe40/resource/101f35d5-547f-4a6f-bdba-0b15771c3a63/download/-2012-2017-.xls > data/traffic/sources/traffic-2012-2016-partial-2017.xls

# unprocessed
curl https://www.odata.org.il/dataset/fa4eecb8-df84-4d49-bf9b-496e493e474b/resource/f9457ee6-ae63-412c-8d64-bd3d2d4cc941/download/-1-9-2012-2015.xls > data/sources/selected-local-1b-small-2012-2015.xls
curl https://www.odata.org.il/dataset/fa4eecb8-df84-4d49-bf9b-496e493e474b/resource/54fd96a2-c13c-4bdd-b467-c5eb6a365e4d/download/-2-2012-2015-.xls > data/sources/selected-local-2a-small-2012-2015.xls
