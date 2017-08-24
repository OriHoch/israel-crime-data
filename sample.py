from datapackage_pipelines_plus_plus.base_processors.base import BaseProcessor
import logging


class Processor(BaseProcessor):

    def _filter_resource(self, resource_number, resource_data):
        sample_size = int(self._parameters.get("sample-size", 5))
        drop_size = int(self._parameters.get("drop-size", 0))
        for row_num, row in enumerate(super(Processor, self)._filter_resource(resource_number, resource_data)):
            if not drop_size or row_num < drop_size:
                yield row
            if row_num == 0:
                logging.info("sampling {} rows from resource {}".format(sample_size,
                                                                        self._get_resource_descriptor(resource_number)["name"]))
            elif row_num < sample_size:
                logging.info(row)


if __name__ == "__main__":
    Processor.main()
