from datapackage_pipelines_plus_plus.base_processors.filter_resource import FilterResourceBaseProcessor
import logging, re


class Processor(FilterResourceBaseProcessor):

    def _get_schema(self, resource_descriptor):
        return {"fields": [{"name": "place_name", "type": "string", "es:type": "keyword"},
                           {"name": "place_type", "type": "string", "es:type": "keyword"},
                           {"name": "year_quarter", "type": "string", "es:type": "keyword"},
                           {"name": "value", "type": "number"},
                           {"name": "source_sheet", "type": "integer"}]}

    def _skip_invalid_row(self, row):
        if row["place_name"].strip() not in ["סכום כולל"]:
            yield row

    def _filter_row(self, row):
        if self._parameters.get("only_schema"):
            yield from self._skip_invalid_row({"place_name": row["place_name"],
                                               "place_type": row["place_type"],
                                               "year_quarter": "{}_{}".format(row["year"], row["quarter"]),
                                               "value": float(row["value"]),
                                               "source_sheet": self._source_sheet})
        else:
            for k in row:
                m = re.match(self._year_quarter_pattern, k)
                if m is not None:
                    year, quarter = map(int, m.groups())
                    yield from self._skip_invalid_row({"place_name": row["place_name"],
                                                       "place_type": row["place_type"],
                                                       "year_quarter": "{}_{}".format(year, quarter),
                                                       "value": float(row[k]) if row[k] else 0,
                                                       "source_sheet": self._source_sheet})

    def _filter_resource(self, resource_data):
        self._year_quarter_pattern = re.compile("^([0-9]{4})_q([0-9])$")
        self._source_sheet = int(self._parameters["source_sheet"])
        yield from super(Processor, self)._filter_resource(resource_data)


if __name__ == "__main__":
    Processor.main()
