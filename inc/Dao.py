from sqlalchemy.inspection import inspect


class Dao:


    def __str__(self):
        instance = str({c: getattr(self, c) for c in inspect(self).attrs.keys()})
        return instance