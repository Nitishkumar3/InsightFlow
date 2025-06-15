import google.generativeai as genai

def GenAI(query):
    try:
        genai.configure(api_key="AIzaSyDTZzFzmpgNeZhy-YSRiPqjx9tzwLpmE0I")
        safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}]
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 2048,

}, safety_settings = safety_settings)
        convo = model.start_chat(history=[])
        convo.send_message(query)
        return convo.last.text.strip()
    except Exception as e:
        return str(e)