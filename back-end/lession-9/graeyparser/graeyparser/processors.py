
class RemoveComma:

    def __call__(self, values: str):
        return [int(i.replace(',', '')) for i in values]
