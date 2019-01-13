import psycopg2
from app.db.connect_web import ConnectDataBase


from_db = ConnectDataBase()


class DataPets:

    def parse_to_json_breeds(self):
        # ['id', 'breed_name', 'section', 'country', 'url', 'image', 'pdf']
        colnames, breeds = from_db.select_breeds()
        not_sorted_breeds_dict = dict()
        for breed in breeds:
            not_sorted_breeds_dict[breed[1]] = {
                colnames[0]: breed[0],
                colnames[2]: breed[2],
                colnames[3]: breed[3],
                colnames[4]: breed[4],
                colnames[5]: breed[5],
                colnames[6]: breed[6]
            }
        breeds_dict = dict(sorted(not_sorted_breeds_dict.items()))
        return breeds_dict

    def parse_to_json(self, function):
        colnames, rows = function
        count_of_cols = len(colnames)
        list_of_pets = list()
        for row in rows:
            part_of_list = dict()
            for one_col in range(0, count_of_cols):
                temp_dict = {
                    colnames[one_col]: row[one_col]
                }
                part_of_list.update(temp_dict)
            list_of_pets.append(part_of_list)
        return list_of_pets

    def add_dog(self, owner, breed, sex, dog_bday, pet_name, kennel):
        try:
            from_db.insert_users_dog_in_db(owner, breed, sex, dog_bday, pet_name, kennel)
            return True
        except psycopg2.Error as e:
            error = e.pgerror
            return False



# a = DataPets()
# print(a.add_dog(owner='user_1', breed='AIREDALE TERRIER', sex='man', dog_bday='2018-01-20', pet_name='Mobi', kennel='Msk mob'))
# print(a.parse_to_json(from_db.select_users_dogs('user_1')))