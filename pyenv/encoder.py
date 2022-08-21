from .env_args import EnvArg, DefaultSeperator


class EnvEncoder:
    def __init__(self, data: dict[str, EnvArg]):
        self.data = data

    def encode(self, seperator: str = DefaultSeperator):
        str_array: list[str] = []
        for field_name, field_value in self.data.items():
            if isinstance(field_value, EnvArg):
                str_array.append(f"{field_name} = {field_value!r}")
            else:
                raise TypeError(
                    f"values must only be of types {EnvArg.__name__!r}")

        return seperator.join(str_array)
