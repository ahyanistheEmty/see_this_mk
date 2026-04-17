import asyncio
from playwright.async_api import async_playwright

async def extract_headlines(url="https://www.bbc.com/news"):
    \"\"\"
    Navigates to a news website using Playwright, extracts main headlines,
    and prints them.
    \"\"\"
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            print(f"Navigating to {url}...")
            await page.goto(url, wait_until="domcontentloaded")
            print("Page loaded. Extracting headlines...")

            # Target h3 tags as they are common for headlines on BBC News
            headline_elements = await page.locator("h3").all()

            headlines = []
            for element in headline_elements:
                text = await element.text_content()
                if text and len(text.strip()) > 5:
                    headlines.append(text.strip())
            
            if headlines:
                print("\n--- Main Headlines ---")
                for i, headline in enumerate(headlines):
                    print(f"{i + 1}. {headline}")
                print("--------------------\n")
            else:
                print("No headlines found with the current selectors.")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(extract_headlines())
