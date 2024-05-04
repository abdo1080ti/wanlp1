from fastapi import FastAPI, HTTPException
from predection import predect_new_category
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

app = FastAPI()

# Enable CORS
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

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--lang=ar')  # Set Arabic as the language

def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text)

def scrape_text_from_url(url):
    try:
        # Create a WebDriver instance
        driver = webdriver.Chrome(options=chrome_options)

        # Scrape article content using BeautifulSoup
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        article = soup.find('article')
        article_text = article.get_text(separator="\n") if article else "Article content not found."

        return remove_extra_spaces(article_text)
    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None
    finally:
        # Close the WebDriver instance
        driver.quit()

@app.post('/categorize', response_model=ClassificationResult)
def predict_category(data: Message):
    user_message = data.message
    print("Received categorize payload:", user_message)  # Log the received payload
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
    # Scrape text from URL
    text = scrape_text_from_url(url)
    if text:
        # Call the classification function and return the results
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
