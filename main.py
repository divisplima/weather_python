import requests
import sys

def print_title(title_str):
    """
    Print a title with a decorative border.

    Args:
        title_str (str): The title string to be printed.
    """
    print("=" * 50)
    print(title_str.center(50))
    print("=" * 50)


def get_city_name():
    """
    Get the name of the city from user input.

    Returns:
        str: The name of the city entered by the user.
    """
    prompt = "Nome da cidade/país: "
    return input(prompt).strip().title()


def get_weather_url(city_name):
    """
    Generate the weather URL based on the city name.

    Args:
        city_name (str): The name of the city.

    Returns:
        str: The complete weather URL.
    """
    base_url = "https://wttr.in/"
    return f"{base_url}{city_name}?m&lang=pt-br"


def get_weather_data(weather_url):
    """
    Get weather data from the provided URL.

    Args:
        weather_url (str): The URL for weather information.

    Returns:
        str: Weather data.
    """
    try:
        response = requests.get(weather_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Ocorreu um erro ao acessar a API: {e}"


def main():
    """
    Main function to execute the weather information retrieval.
    """
    while True:
        print_title("PREVISÃO DO TEMPO v.1.0")
        city_name = get_city_name()
        weather_url = get_weather_url(city_name)
        data = get_weather_data(weather_url)

        if "Ocorreu um erro" in data:
            print(data)
        else:
            print(data)

        response = input("Gostaria de verificar o clima de outra cidade/país? (s/n): ")
        if response.lower() == 'n' or response.lower() != 's':
            print_title("PROGRAMA ENCERRADO")
            sys.exit()


if __name__ == "__main__":
    main()
