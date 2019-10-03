from dataclasses import dataclass


@dataclass
class InstagramItem:
    photo_id: str
    photo_link: str

    @staticmethod
    def retrieve_list(list):
        result = []
        for item in list:
            result.append(InstagramItem(item[0], item[1]))
        return result
