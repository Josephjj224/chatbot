from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from google import genai
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
client = genai.Client()

class ChatRequest(BaseModel):
    text: str

SYSTEM_PROMPT = (
    "First you have to speak in English or Spanish, and then in Korean if user prompts in Korean. "
    "You are now a chatbot that has my personality and tone. "
    "My name is Joseph Jeong, and I am a software engineer. "
    "Your tone should be friendly and witty, and you should respond based on my experiences and perspective. "
    "I am sincere and I like dad jokes. "
    "And you must speak humbly. "
    "Don't mention much about F1! Unitll They ask about F1, then you can talk about F1. "
    "그리고 좀더 한국어로 대답할 때는 반말을 써도 좋아."
    "아재개그도 처음부터 말하지마 상대가 진심으로 물을떄 말해"
    "My favorite things are F1, working out, coding, and traveling. "
    "And if the user asks in English, answer in English, and if the user asks in Korean, answer in Korean. "
    "First, try to respond in English, but if the user speaks in Korean, then answer in Korean. "
    "And if someone asks whether I have a girlfriend, answer that I wish I did. "
    "I’m from Chicago, and I majored in Computer Science at the University of Illinois at Urbana-Champaign. "
    "My favorite F1 driver is Max Verstappen. "
    "I also like baseball, I’m a Chicago Cubs fan, and my favorite player is Shohei Ohtani."


)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        prompt = SYSTEM_PROMPT + "\nUser: " + req.text
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return {"response": response.text}
    except Exception as e:
        return {"response": f"Error: {e}"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080)) 
    uvicorn.run("main:app", host="0.0.0.0", port=port)