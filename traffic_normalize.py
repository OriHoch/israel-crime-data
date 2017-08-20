from datapackage_pipelines_plus_plus.base_processors.filter_resource import FilterResourceBaseProcessor
import logging, re


class Processor(FilterResourceBaseProcessor):

    @classmethod
    def _get_schema(cls):
        return {"fields": [{"name": "place_name", "type": "string"},
                           {"name": "place_type", "type": "string"},
                           {"name": "year", "type": "integer"},
                           {"name": "quarter", "type": "integer"},
                           {"name": "value", "type": "number"}],
                "primaryKey": ["place_name", "place_type", "year", "quarter"]}

    def _skip_invalid_row(self, row):
        if row["place_name"].strip() not in ["סכום כולל"]:
            yield row

    def _filter_row(self, row):
        if self._parameters.get("only_schema"):
            yield from self._skip_invalid_row({"place_name": row["place_name"],
                                               "place_type": row["place_type"],
                                               "year": int(float(row["year"])),
                                               "quarter": int(float(row["quarter"])),
                                               "value": float(row["value"])})
        else:
            for k in row:
                m = re.match(self._year_quarter_pattern, k)
                if m is not None:
                    year, quarter = map(int, m.groups())
                    yield from self._skip_invalid_row({"place_name": row["place_name"],
                                                       "place_type": row["place_type"],
                                                       "year": year,
                                                       "quarter": quarter,
                                                       "value": float(row[k]) if row[k] else 0})

    def _filter_resource(self, resource_data):
        self._year_quarter_pattern = re.compile("^([0-9]{4})_q([0-9])$")
        yield from super(Processor, self)._filter_resource(resource_data)


if __name__ == "__main__":
    Processor.main()
