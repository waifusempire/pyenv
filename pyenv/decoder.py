from .env_args import DefaultSeperator


class EnvDecoder:
    def __init__(self, data: str):
        self.data = data

    def decode(self):
        _data = self.data
        lines = _data.splitlines(False)
        _dict = {}
        data = [line.split(" = ") for line in lines]
        for name, val in data:
            _dict.update({name: val})
        return self.converter(_dict)

    def converter(self, data: dict[str, str]):
        new_data = dict()
        for name, val in data.items():
            if (val.startswith("'") and val.endswith("'")):
                val = val.removeprefix("'").removesuffix("'")
                new_data.update({name: val})
                continue
            elif (val.startswith("\"") and val.endswith("\"")):
                val = val.removeprefix("\"").removesuffix("\"")
                new_data.update({name: val})
                continue
            elif val == "True":
                val = True
                new_data.update({name: val})
                continue
            elif val == "False":
                val = False
                new_data.update({name: val})
                continue
            elif val == "None":
                val = None
                new_data.update({name: val})
                continue
            elif "." in val:
                val = float(val)
                new_data.update({name: val})
                continue
            else:
                try:
                    val = int(val)
                except Exception:
                    val = val
                new_data.update({name: val})
                continue

        return new_data
