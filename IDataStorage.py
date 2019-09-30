from abc import ABC, abstractmethod


class IDataStorage(ABC):
    @abstractmethod
    def get_objects(self):
        pass

    @abstractmethod
    def get_object(self, key):
        pass

    @abstractmethod
    def put_object(self, key, value):
        pass

    @abstractmethod
    def delete_object(self, key):
        pass
