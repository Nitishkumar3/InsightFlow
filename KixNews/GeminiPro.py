import google.generativeai as genai

def GenAI(query, model_name="gemini-1.5-flash", max_output_tokens = 2048):
    try:
        genai.configure(api_key="AIzaSyD7mVT4Weocjl9_NzLaMk5F9eJFmru_P_Q")
        safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}]
        model = genai.GenerativeModel(model_name=model_name, generation_config = {"temperature": 1, "top_p": 0.95, "top_k": 64, "max_output_tokens": max_output_tokens,}, safety_settings = safety_settings)
        convo = model.start_chat(history=[])
        convo.send_message(query)
        return convo.last.text.strip()
    except Exception as e:
        return str(e)