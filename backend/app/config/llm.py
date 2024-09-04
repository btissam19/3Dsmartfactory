from langchain_google_genai import GoogleGenerativeAI
llm = GoogleGenerativeAI(model="gemini-1.5-flash",google_api_key="AIzaSyAz4mqqTvqCJ49E7Xv7tuvku-w68kVhjxk",generation_config={"response_mime_type": "application/json"})



