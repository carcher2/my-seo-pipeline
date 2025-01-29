import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("SEMRUSH_API_KEY")

if not api_key:
    raise ValueError("SEMRUSH_API_KEY is not set in your .env file!")

def test_keyword_overview():
    """Test basic connectivity to SEMrush API using Keyword Overview endpoint"""
    
    # Base URL for SEMrush API
    base_url = "https://api.semrush.com"
    
    # Using the Keyword Overview endpoint (costs 10 API units per line)
    params = {
        'type': 'phrase_this',  # For single database keyword overview
        'key': api_key,
        'phrase': 'seo',  # Test keyword
        'database': 'us',  # US database
        'export_columns': 'Ph,Nq,Cp,Co,Nr,Td',  # Basic keyword metrics
        'export_decode': 1  # Don't URL encode the response
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        print("\nSuccessfully connected to SEMrush API!")
        print("Response status code:", response.status_code)
        print("\nSample response data:")
        print(response.text[:500])
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"\nError connecting to SEMrush API: {e}")
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            print("Error details:", e.response.text)
        return False

if __name__ == "__main__":
    test_keyword_overview() 