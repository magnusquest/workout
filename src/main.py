package = "workout"
import streamlit as st
from profiles import create_profile, get_notes, get_profile
from form_submit import update_personal_info, add_note, delete_note
from ai import get_macros, ask_ai

st.title('Personal Fitness Tool')

@st.fragment
def personal_data_form():
    with st.form("personal_data_form"):
        st.header = "Personal Data"

        profile = st.session_state.profile

        name = st.text_input("Name", value=profile["general"]["name"])
        age = st.number_input("Age", min_value=0, max_value=120, step=1, value=profile["general"]["age"])
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=1000.0, step=0.1, value=float(profile["general"]["weight"]))
        height = st.number_input("Height (cm)", min_value=0.0, max_value=300.0, step=0.1, value=float(profile["general"]["height"]))

        genders = ["Male", "Female"]
        gender = st.radio("Gender", genders, index=genders.index(profile["general"].get("gender", "Male")))

        activities = ("Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Super Active")
        activity_level = st.selectbox("Activity Level", activities, index=activities.index(profile["general"].get("activity_level", "Moderately Active")))

        submitted = st.form_submit_button("Submit")
        if submitted:
            if all([name, age, weight, height, gender, activity_level]):
                with st.spinner("Processing..."):
                    st.session_state.profile = update_personal_info(profile, "general", name=name, age=age, weight=weight, height=height, gender=gender, activity_level=activity_level)
                    st.success("Personal data submitted")
            else: 
                st.error("Please fill in all fields")

@st.fragment
def goals_form():
    profile = st.session_state.profile
    with st.form("goals_form"):
        st.header = "Goals"

        goals = st.multiselect("Goals", ["Muscle gain", "Fat loss", "Endurance", "Strength"], default=profile.get("goals", []))

        submitted = st.form_submit_button("Submit")
        if submitted:
            if goals:
                with st.spinner("Processing..."):
                    st.session_state.profile = update_personal_info(profile, "goals", goals=goals)
                    st.success("Goals submitted")
            else:
                st.warning("Please select at least one goal")

@st.fragment
def macros():
    profile = st.session_state.profile
    nutrition = st.container(border=True)
    nutrition.header("Macros")
    if nutrition.button("Generate with AI"):
        result = get_macros(profile.get("general", ""), profile.get("goals", ""))
        profile["nutrition"] = result
        nutrition.success("Macros generated")

    with nutrition.form("nutrition_form", border=False):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            calories = st.number_input("Calories", min_value=0, max_value=10000, step=1, value=profile["nutrition"].get("calories", 0))
        with col2:
            protein = st.number_input("Protein (g)", min_value=0, max_value=1000, step=1, value=profile["nutrition"].get("protein", 0))
        with col3:
            fat = st.number_input("Fat (g)", min_value=0, max_value=1000, step=1, value=profile["nutrition"].get("fat", 0))
        with col4:
            carbs = st.number_input("Carbs (g)", min_value=0, max_value=1000, step=1, value=profile["nutrition"].get("carbs", 0))

        if st.form_submit_button("Submit"):
            with st.spinner("Processing..."):
                st.session_state.profile = update_personal_info(profile, "nutrition", calories=calories, protein=protein, fat=fat, carbs=carbs)
                st.success("Macros submitted")


def forms():
    if "profile" not in st.session_state:
        profile_id = 1
        profile = get_profile(profile_id)
        if not profile:
            profile_id, profile = create_profile(profile_id)

        st.session_state.profile = profile
        st.session_state.profile_id = profile_id

    if "notes" not in st.session_state:
        notes = get_notes(st.session_state.profile_id)
        st.session_state.notes = notes

    personal_data_form()
    goals_form()
    macros()



if __name__ == "__main__":
    forms()