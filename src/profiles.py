from db import personal_data_collection, notes_collection

def get_values(_id):
    return {
        "_id": _id,
        "general": {
            "name": "John Doe",
            "age": 30,
            "weight": 80.0,
            "height": 180.0,
            "activity_level": "Moderately Active",
            "gender": "Male"
        },
        "goals": ["Muscle gain"],
        "nutrition": {
            "calories": 2000,
            "protein": 150,
            "carbs": 200,
            "fat": 70
        },
    }

def create_profile(_id):
    profile_values = get_values(_id)
    result = personal_data_collection.insert_one(profile_values)
    return result.inserted_id, profile_values

def get_profile(_id):
    return personal_data_collection.find_one({"_id": {"$eq": _id}})

def get_notes(_id):
    return list(notes_collection.find({"user_id": {"$eq": _id}}))