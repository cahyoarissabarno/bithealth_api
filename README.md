# Hospital Triage Department Recommendation API

This API service recommends a hospital department based on patient gender, age, and symptoms using the Gemini LLM via LangChain. It assists non-medical staff in triaging patients by suggesting the most relevant department, reducing wait times and human error.

## Available Departments
The service recommends one of the following departments based on patient symptoms, gender, and age:

- **Neurology**: Specializes in brain, spinal cord, and nervous system disorders. Treats symptoms like pusing (dizziness), sakit kepala (headache), sulit berjalan (difficulty walking), kehilangan keseimbangan (loss of balance), kejang (seizures), or kesemutan (numbness/tingling).
- **Cardiology**: Focuses on heart and blood vessel conditions. Manages symptoms such as nyeri dada (chest pain), sesak napas (shortness of breath), jantungan (palpitations), pingsan (fainting), or kaki bengkak (swollen legs due to heart issues).
- **Gastroenterology**: Addresses digestive system disorders (stomach, intestines, liver). Handles symptoms like mual (nausea), muntah (vomiting), sakit perut (abdominal pain), diare (diarrhea), sembelit (constipation), or perut kembung (bloating).
- **Pulmonology**: Treats lung and respiratory system diseases. Manages symptoms including batuk (cough), sesak napas (shortness of breath), demam (fever with respiratory issues), mengi (wheezing), or dahak berdarah (blood in sputum).
- **Orthopedics**: Deals with musculoskeletal system (bones, joints, muscles). Treats symptoms like nyeri sendi (joint pain), nyeri punggung (back pain), sulit berjalan (difficulty walking due to joint/muscle issues), patah tulang (fractures), or kaku sendi (joint stiffness).
- **Endokrinologi**: Manages hormone-related disorders (thyroid, diabetes, etc.). Handles symptoms such as lelah berlebihan (excessive fatigue), haus berlebihan (excessive thirst), sering kencing (frequent urination), berat badan turun tiba-tiba (sudden weight loss), or tremor (tremors).
- **Psikiatri**: Focuses on mental health and behavioral disorders. Treats symptoms like susah tidur (insomnia), cemas berlebihan (excessive anxiety), sedih berkepanjangan (prolonged sadness), halusinasi (hallucinations), or sulit konsentrasi (difficulty concentrating).
- **Dermatologi**: Specializes in skin, hair, and nail conditions. Manages symptoms including gatal (itching), ruam kulit (skin rash), kemerahan (redness), jerawat parah (severe acne), or luka tidak sembuh (non-healing sores).

## Prerequisites
- Python 3.8+
- Google AI Studio API key (get it from https://aistudio.google.com)

## Setup
1. **Clone or create the project**:
   - Save `main.py`, `requirements.txt`, `.env.example`, and `README.md` in a project directory (e.g., `triage_service`).

2. **Install dependencies**:
   - Install required libraries using `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set environment variable**:
   - Copy `.env.example` to `.env` and add your Google API key:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` to include your API key, e.g.:
     ```
     GOOGLE_API_KEY=your-api-key-here
     ```
   - Alternatively, export the key manually:
     ```bash
     export GOOGLE_API_KEY='your-api-key-here'
     ```
   - On Windows, use:
     ```cmd
     set GOOGLE_API_KEY=your-api-key-here
     ```
   - Verify the key is set:
     ```bash
     echo $GOOGLE_API_KEY
     ```

## Running the App
1. **Start the FastAPI server**:
   ```bash
   python main.py
   ```
   - The server runs on `http://localhost:8000`.
   - If you see an error about `GOOGLE_API_KEY`, ensure it’s set correctly in `.env` or as an environment variable.

2. **Test the endpoint**:
   - Use `curl`, Postman, or similar to send a POST request:
     ```bash
     curl -X POST "http://localhost:8000/recommend" -H "Content-Type: application/json" -d '{"gender": "female", "age": 62, "symptoms": ["pusing", "mual", "sulit berjalan"]}'
     ```
   - Expected response:
     ```json
     {"recommended_department": "Neurology"}
     ```
