from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import google.generativeai as genai

genai.configure(api_key="")  # Replace with your API key

def ask_gemini_api(prompt):
    #Sends a prompt to the Gemini API and returns the response
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  # Or other model
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    url = "https://www.wordsearchwebsite.com" #Replace with other website

    try:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        wait = WebDriverWait(driver, 45)


        letter_elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".wordSearchLetters")) #Replace with real CSS selector
        )

        letters = []
        for element in letter_elements:
            letter = wait.until(EC.visibility_of(element)).text.strip()  # Wait for text to be visible
            letters.append(letter)

        #----------------------------------

        hint_elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".wordSearchHint")) #Replace with real CSS selector
        )

        hint = []
        for element in hint_elements:
            hint_text = wait.until(EC.visibility_of(element)).text.strip()
            hint.append(hint_text)

        #----------------------------------

        num_words = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".wordSearchNumberOfWords")) #Replace with real CSS selector
        )

        words = []
        for element in num_words:
            num = wait.until(EC.visibility_of(element)).text.strip()
            words.append(num)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()

    hint = str(hint)
    letters = " ".join(letters)
    words = str(words)

    prompt = (f"Hint: {hint}. Letters: {letters}. Least amount of words: {words}. "
              f"Find as many words as you can that fit the hint and are greater than 3 letters in length "
              f"using only the letters provided.")

    print(ask_gemini_api(prompt))