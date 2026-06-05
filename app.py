import streamlit as st
import pickle

# Load model
with open("intent_model.pkl", "rb") as file:
    model = pickle.load(file)

# Department routing
routes = {
    "Payment Failed": "Payments Support Team",
    "Refund Request": "Refund Team",
    "Cancel Subscription": "Subscription Team",
    "Billing Issue": "Billing Team",
    "Account Verification": "KYC / Verification Team",
    "Card Issue": "Card & Bank Support Team",
    "Fraud Issue": "Fraud Detection Team",
    "Technical Issue": "Technical Support Team",
    "General Support": "General Help Desk"
}

st.set_page_config(page_title="User Intent Classifier")

st.title("Real-Time User Intent Classification")
st.write("This app predicts what the user wants to do while they are typing.")

user_text = st.text_input("Start typing your query:")

if user_text:
    prediction = model.predict([user_text])[0]
    department = routes[prediction]

    st.subheader("Predicted Intent:")
    st.success(prediction)

    st.subheader("Routed To:")
    st.info(department)
else:
    st.warning("Type something to predict intent.")
