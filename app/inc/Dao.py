from app import db
from exception import ResponseException


class Dao:


    @classmethod
    def read_all(cls):
        exist = cls.query.all()
        db.session.close()
        if exist:
            return [instance.as_dict() for instance in exist]

        return exist


    @classmethod
    def read(cls, class_id):
        result_class = cls.query.get(class_id)
        db.session.close()
        if not result_class:
            return None

        return result_class.as_dict()


    def create(self):
        data = self.as_dict()
        data.pop('id')
        
        query = self.__class__(**data)
        db.session.add(query)
        db.session.commit()
        instance = self.as_dict()
        instance.update({'id': query.id})
        db.session.close()
        return instance



    def update(self):
        instance = self.as_dict()
        class_id = instance.pop('id')

        old_class = self.__class__.query.get(class_id)
        if not old_class:
            db.session.close()
            raise ResponseException(f'{self.__class__.__name__}.id: {class_id}', 404)

        for k, v in instance.items():
            setattr(old_class, k, v)

        db.session.commit()
        db.session.close()
        return self.as_dict()


    @classmethod
    def delete(cls, class_id):
        instance = cls.query.get(class_id)
        if not instance:
            raise ResponseException(f'{cls.__name__}.id: {class_id}', 404)

        db.session.delete(instance)
        db.session.commit()
        db.session.close()
        return instance.as_dict()
