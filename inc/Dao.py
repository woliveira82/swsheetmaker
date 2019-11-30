
from app import db
from flask_sqlalchemy import inspect

class Dao:


    @classmethod
    def read_all(cls):
        try:
            exist = cls.query.all()
            if len(exist) == 0:
                return {'response': [], 'status': 404}

            return {'response': [i for i in exist], 'status': 200}

        except Exception as e:
            return {'response': [str(e)], 'status': 406}

        finally:
            db.session.close()


    @classmethod
    def read(cls, class_id):
        try:
            result_class = cls.query.get(class_id)

            if not result_class:
                return {'response': 'Not found', 'status': 404}

            return {'response': result_class, 'status': 200}

        except Exception as e:
            return {'response': str(e), 'status': 406}

        finally:
            db.session.close()


    def create(self):
        data = self.as_dict()
        data.pop('id')
        try:
            query = self.__class__(**data)
            db.session.add(query)
            db.session.commit()
            self.__id = query.id
            return {'response': self.as_dict(), 'status': 201}

        except Exception as e:
            db.session.rollback()
            return {'response': str(e), 'status': 406}

        finally:
            db.session.close()


    def update(self):
        search = { 'id': self.id }
        try:
            result = self.__class__.query.filter_by(**search).update(**self.as_dict())
            if result == 0:
                return {'response': 'Resource not found', 'status': 404}

            db.session.commit()
            return {'response': self.as_dict(), 'status': 200}

        except Exception as e:
            db.session.rollback()
            return {'response': str(e), 'status': 406}

        finally:
            db.session.close()


    def delete(self):
        search = { 'id': self.id }
        try:
            query = self.__class__.query.filter_by(**search).first()
            if search is None:
                return {'response': 'Resource not found', 'status': 404}

            db.session.delete(query)
            db.session.commit()
            response = {'response': self.as_dict(), 'status': 200}
            self = None
            return response

        except Exception as e:
            db.session.rollback()
            return {'response': str(e), 'status': 406}
            
        finally:
            db.session.close()
