#!/usr/bin/python3
""" Start of implementation of almost a circle """


class Base:
    """ parent class for all classes in project """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ imports a list of dictionaries into json format """
        import json

        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json string rep of list of objects to a file """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as myFile:
            list_dictionaries = []
            if list_objs is None:
                myFile.write("[]")
            else:
                list_dictionaries = [iter.to_dictionary() for iter in list_objs]
            myFile.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ method to return the list of the JSON string rep from json_string """
        import json

        if json_string is None or len(json_string) is 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates a base instance with all attributes set """
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns lists of instances dependent on the class """
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as myFile:
                list_json = cls.from_json_string(myFile.read())
        except FileNotFoundError:
            return []
        return [cls.create(**kwargs) for kwargs in list_json]
