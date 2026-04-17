import urllib.parse
from playwright.sync_api import sync_playwright

def perform_google_search(query):
    print(f"Searching for: {query}...")
    
    with sync_playwright() as p:
        # Launching headless browser for efficiency
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Encode the query and navigate to Google Search
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?q={encoded_query}"
        page.goto(url, wait_until="domcontentloaded")
        
        # Locate all h3 elements (standard for search result titles)
        result_elements = page.locator("h3").all()
        
        top_results = []
        for element in result_elements[:3]:
            title = element.inner_text()
            # Extract the URL from the nearest parent 'a' tag
            link = element.evaluate("el => el.closest('a').href")
            top_results.append({"title": title, "url": link})
            
        browser.close()
        return top_results

if __name__ == "__main__":
    user_query = input("Enter your search query: ")
    results = perform_google_search(user_query)
    
    if results:
        print("\nTop 3 Results:")
        for i, res in enumerate(results, 1):
            print(f"{i}. {res['title']}")
            print(f"   URL: {res['url']}\n")
    else:
        print("No results found.")
