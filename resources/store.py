from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message':'Store not found!'}, 404


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message':f'Store with name `{name}` already exists!'}

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occurred!'}, 500

        return store.json(), 201


    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message':f'A store `{name}` was deleted!'}, 200

class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}