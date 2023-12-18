import requests
from bs4 import BeautifulSoup

# Function to check if a Steam Workshop mod has any requirements
def check_mod_requirements(mod_url):
    try:
        # Send an HTTP GET request to the mod's URL
        response = requests.get(mod_url)
        response.raise_for_status()

        # Parse the HTML content of the mod's page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the section with mod requirements (based on the provided page structure)
        requirements_section = soup.find('div', {'class': 'requiredItemsContainer'})

        if requirements_section:
            # Find all requiredItem divs containing requirement names
            requirements_list = requirements_section.find_all('div', {'class': 'requiredItem'})

            if requirements_list:
                print("This mod has the following requirements:")
                for requirement in requirements_list:
                    requirement_name = requirement.text.strip()  # Remove extra spaces and newlines
                    print(requirement_name)
            else:
                print("This mod has no requirements.")
        else:
            print("Unable to find mod requirements on this page.")

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# Example usage
mod_url = "https://steamcommunity.com/sharedfiles/filedetails/?id=2200148440"
check_mod_requirements(mod_url)
