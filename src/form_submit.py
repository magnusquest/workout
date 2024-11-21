from datetime import datetime as dt
from db import personal_data_collection, notes_collection

def update_personal_info(profile, update_type, **kwargs):
    if update_type == "goals":
        profile["goals"] = kwargs.get("goals", [])
        update_field = {"goals": profile["goals"]}
    else:
        profile[update_type] = kwargs
        update_field = {update_type: profile[update_type]}

    personal_data_collection.update_one({"_id": profile["_id"]}, {"$set": update_field})

    return profile

def add_note(note, profile_id):
    new_note = {"user_id": profile_id, "text": note, "$vectorize": note, "metadata": {"injested": dt.now()}}
    result = notes_collection.insert_one(new_note)
    new_note["_id"] = result.inserted_id
    return new_note

def delete_note(note_id):
    notes_collection.delete_one({"_id": note_id})