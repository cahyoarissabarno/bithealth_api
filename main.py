from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Pydantic model for request body
class PatientInfo(BaseModel):
    gender: str
    age: int
    symptoms: list[str]

# Initialize LLM (Gemini via Google AI Studio)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# Define prompt template
prompt = PromptTemplate(
    input_variables=["gender", "age", "symptoms"],
    template="""
    Given a patient with:
    - Gender: {gender}
    - Age: {age}
    - Symptoms: {symptoms}

    Recommend the most relevant hospital department for triage from the following list only:
    - Neurology: Specializes in brain, spinal cord, and nervous system disorders. Treats symptoms like pusing (dizziness), sakit kepala (headache), sulit berjalan (difficulty walking), kehilangan keseimbangan (loss of balance), kejang (seizures), or kesemutan (numbness/tingling).
    - Cardiology: Focuses on heart and blood vessel conditions. Manages symptoms such as nyeri dada (chest pain), sesak napas (shortness of breath), jantungan (palpitations), pingsan (fainting), or kaki bengkak (swollen legs due to heart issues).
    - Gastroenterology: Addresses digestive system disorders (stomach, intestines, liver). Handles symptoms like mual (nausea), muntah (vomiting), sakit perut (abdominal pain), diare (diarrhea), sembelit (constipation), or perut kembung (bloating).
    - Pulmonology: Treats lung and respiratory system diseases. Manages symptoms including batuk (cough), sesak napas (shortness of breath), demam (fever with respiratory issues), mengi (wheezing), or dahak berdarah (blood in sputum).
    - Orthopedics: Deals with musculoskeletal system (bones, joints, muscles). Treats symptoms like nyeri sendi (joint pain), nyeri punggung (back pain), sulit berjalan (difficulty walking due to joint/muscle issues), patah tulang (fractures), or kaku sendi (joint stiffness).
    - Endokrinologi: Manages hormone-related disorders (thyroid, diabetes, etc.). Handles symptoms such as lelah berlebihan (excessive fatigue), haus berlebihan (excessive thirst), sering kencing (frequent urination), berat badan turun tiba-tiba (sudden weight loss), or tremor (tremors).
    - Psikiatri: Focuses on mental health and behavioral disorders. Treats symptoms like susah tidur (insomnia), cemas berlebihan (excessive anxiety), sedih berkepanjangan (prolonged sadness), halusinasi (hallucinations), or sulit konsentrasi (difficulty concentrating).
    - Dermatologi: Specializes in skin, hair, and nail conditions. Manages symptoms including gatal (itching), ruam kulit (skin rash), kemerahan (redness), jerawat parah (severe acne), or luka tidak sembuh (non-healing sores).

    Based on the symptoms, gender, and age, select the most appropriate department from the list above. Return only the department name as a single word or phrase (e.g., Neurology).
    """
)

# Create LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

@app.post("/recommend")
async def recommend_department(patient: PatientInfo):
    try:
        # Run LLM chain to get department
        department = chain.run(
            gender=patient.gender,
            age=patient.age,
            symptoms=", ".join(patient.symptoms)
        ).strip()
        return {"recommended_department": department}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)