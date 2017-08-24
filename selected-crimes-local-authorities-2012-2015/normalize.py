from datapackage_pipelines_plus_plus.base_processors.filter_resource import FilterResourceBaseProcessor
import logging, re


class Processor(FilterResourceBaseProcessor):

    def _get_schema(self, resource_descriptor):
        return {"fields": [{"name": "resource", "type": "string", "es:type": "keyword"},
                           {"name": "place_name", "type": "string", "es:type": "keyword"},
                           {"name": "stat_region_code", "type": "string", "es:type": "keyword"},
                           {"name": "stat_group", "type": "string", "es:type": "keyword"},
                           {"name": "stat_offence", "type": "string", "es:type": "keyword"},
                           {"name": "year_quarter", "type": "string", "es:type": "keyword"},
                           {"name": "value", "type": "number"},]}

    def _filter_row(self, resource_number, row):
        for k in row:
            m = re.match(self._year_quarter_pattern, k)
            if m is not None:
                year, quarter = map(int, m.groups())
                resource = self._get_output_resource_name()
                place_name = row["place_name"]
                stat_region_code = row["stat_region_code"]
                stat_group = row["stat_group"]
                stat_offence = row["stat_offence"]
                year_quarter = "{}_{}".format(year, quarter)
                keys = [str(v).strip().lower() for v in [year_quarter, place_name, stat_region_code,
                                                         stat_group, stat_offence]]
                if "total" in keys:
                    continue
                if not row[k] or str(row[k]).strip().lower() in [""]:
                    value = 0
                else:
                    value = float(row[k])
                yield {"resource": resource,
                       "place_name": place_name,
                       "stat_region_code": stat_region_code,
                       "stat_group": stat_group,
                       "stat_offence": stat_offence,
                       "year_quarter": year_quarter,
                       "value": value}

    def _filter_resource(self, resource_number, resource_data):
        self._year_quarter_pattern = re.compile("^([0-9]{4})_q([0-9])$")
        yield from super(Processor, self)._filter_resource(resource_number, resource_data)


if __name__ == "__main__":
    Processor.main()
