from pathlib import Path

from eva.analysis import (
    annual_hours,
    compare_countries,
    countries,
    country_total,
    cumulative_hours,
)
from eva.charts import plot_annual, plot_cumulative, show_charts
from eva.cli import (
    print_comparison,
    print_country_total,
    prompt_country,
    prompt_known_country,
    prompt_year_range,
)
from eva.loader import load_evas
from eva.preparation import prepare

DATA_PATH = Path("eva-data.json")
CUMULATIVE_CHART_PATH = Path("cumulative_duration.png")
ANNUAL_CHART_PATH = Path("annual_duration.png")


def main() -> None:
    records = prepare(load_evas(DATA_PATH))

    country = prompt_country()
    print_country_total(country, country_total(records, country))

    known = countries(records)
    print("\nCompare EVA activity between two countries")
    first = prompt_known_country("Country A: ", known)
    second = prompt_known_country("Country B: ", known)
    years = prompt_year_range()
    print_comparison(compare_countries(records, first, second, years))

    plot_cumulative(*cumulative_hours(records), CUMULATIVE_CHART_PATH)
    plot_annual(annual_hours(records), ANNUAL_CHART_PATH)
    show_charts()


if __name__ == "__main__":
    main()
