def prompt_country() -> str:
    return input("Enter a country: ")


def print_country_total(country: str, total_hours: float) -> None:
    print(f"Total EVA duration for {country}: {total_hours:.2f} hours")
