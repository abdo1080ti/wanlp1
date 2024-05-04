from fastapi import FastAPI, HTTPException
from predection import predect_new_category
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from web_scraping import scrape_text_from_url  

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

class ClassificationResult(BaseModel):
    main_category: str
    main_probability: float
    subcategories: list

@app.post('/categorize', response_model=ClassificationResult)
def predict_category(data: Message):
    user_message = data.message
    print("Received categorize payload:", user_message)  
    article = [user_message]
    try:
        category_set, max_category, all_category_probabilities, other = predect_new_category(article)
        main_category, main_probability = max(all_category_probabilities, key=lambda x: x[1])
        subcategories = [(category, probability) for category, probability in all_category_probabilities if category != main_category]
        return {
            'main_category': main_category,
            'main_probability': main_probability,
            'subcategories': subcategories
        }
    except Exception as e:
        print(f"An error occurred during categorization: {e}")
        raise HTTPException(status_code=500, detail="Failed to categorize the article.")

@app.post("/scrape_and_classify")
async def scrape_and_classify(url: str):
    
    text = scrape_text_from_url(url)
    if text:
        
        try:
            category_set, max_category, all_category_probabilities, other = predect_new_category([text])
            main_category, main_probability = max(all_category_probabilities, key=lambda x: x[1])
            subcategories = [(category, probability) for category, probability in all_category_probabilities if category != main_category]
            return {
                'main_category': main_category,
                'main_probability': main_probability,
                'subcategories': subcategories
            }
        except Exception as e:
            print(f"An error occurred during categorization: {e}")
            raise HTTPException(status_code=500, detail="Failed to categorize the article.")
    else:
        raise HTTPException(status_code=400, detail="Failed to scrape text from URL.")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
