from IDataStorage import IDataStorage
import glob
import json


class FileStorage(IDataStorage):
    def __init__(self):
        self._folder = 'storage/'

    def get_objects(self):
        """
        Отдает все json объекты
        :return: Список json объектов
        """
        files = []
        for file_path in glob.glob(self._folder + '*.json'):
            _f = open(file_path)
            file = _f.read()
            files.append(file)

        return files

    def get_object(self, file_id):
        """
        По id возвращает json объект
        :param file_id: id объекта
        :return: json объект
        """
        _f = open(self._folder + file_id + '.json')
        return _f.read()

    def put_object(self, file_id, value):
        """
        Добавляет файл json объекта
        :param file_id: id объекта
        :param value: json объект
        :return: флаг выполнения
        """
        try:
            with open(self._folder + file_id + '.json', 'w') as json_file:
                json_file.write(value)
        except Exception:
            return False
        return True

    def delete_object(self, key):
        pass


if __name__ == '__main__':
    test = FileStorage()
    result = test.get_objects()
    print(result)

    print(test.get_object('temp1'))
    print(test.put_object('temp2', json.dumps(dict(key2='value2'))))
