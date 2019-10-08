from dataclasses import dataclass, asdict


@dataclass
class InstagramItem:
    photo_id: str
    photo_link: str
    user_id: str
    created_time: str

    def __eq__(self, other):
        if self.photo_id == other.photo_id:
            return True
        else:
            return False

    @staticmethod
    def retrieve_list(list):
        result = []
        for item in list:
            if isinstance(item, dict):
                result.append(InstagramItem(item['id'], item['images']['low_resolution']['url'],
                                            item['user']['id'], item['created_time']))
            else:
                result.append(InstagramItem(item[0], item[1], item[2], item[3]))
        return result

    @staticmethod
    def compare_and_save_to_db(media_data, db_data, db):
        for media_item in media_data:
            if media_item not in db_data:
                db.insert_photo(media_item.photo_id, media_item.photo_link, media_item.user_id, media_item.created_time)

    def convert_to_dict(self):
        return asdict(self)
