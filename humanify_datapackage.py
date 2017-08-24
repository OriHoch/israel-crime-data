from datapackage_pipelines_plus_plus.base_processors.base import BaseProcessor
import logging, os, json


README_MD_TEMPLATE = "# {name}\n\n" \
                     "{description}"


class Processor(BaseProcessor):

    def _filter_resources(self, resources):
        yield from super(Processor, self)._filter_resources(resources)
        out_path = lambda relpath: os.path.join(self._parameters["out-path"], relpath)
        if os.path.exists(out_path("README.md")):
            logging.warning("README.md already exists, will not overwrite")
        else:
            with open(out_path("README.md"), "w") as f:
                f.write(README_MD_TEMPLATE.format(name=self._datapackage.get("name", ""),
                                                  description=self._datapackage.get("description", "")))
        with open(out_path("datapackage.json"), "w") as f:
            json.dump(self._datapackage ,f, indent=2, sort_keys=True)


if __name__ == "__main__":
    Processor.main()
