import altair as alt
import pandas as pd


def get_colors() -> dict:
    # Thanks ChatGPT
    return {
        "French": "#1f77b4",  # Blue
        "German": "#ff7f0e",  # Orange
        "Dutch": "#2ca02c",  # Green
        "Danish": "#d62728",  # Red
        "Italian": "#9467bd",  # Purple
        "English": "#8c564b",  # Brown
        "Swedish": "#e377c2",  # Pink
        "Luxembourgish": "#7f7f7f",  # Gray
        "Norwegian": "#bcbd22",  # Olive
        "Finnish": "#17becf",  # Cyan
        "Spanish": "#1f78b4",  # Blue (darker)
        "Serbo-Croatian": "#ff9896",  # Pink (lighter)
        "Portuguese": "#98df8a",  # Green (lighter)
        "Slovene": "#c5b0d5",  # Purple (lighter)
        "Viennese": "#c49c94",  # Brown (lighter)
        "Maltese": "#f7b6d2",  # Pink (lighter)
        "Irish": "#c7c7c7",  # Gray (lighter)
        "Hebrew": "#ffbb78",  # Orange (lighter)
        "Greek": "#2ca02c",  # Green (reused)
        "Turkish": "#d62728",  # Red (reused)
        "Arabic": "#8c564b",  # Brown (reused)
        "Northern Sami": "#17becf",  # Cyan (reused)
        "Icelandic": "#7f7f7f",  # Gray (reused)
        "Romansh": "#bcbd22",  # Olive (reused)
        "Neapolitan": "#1f77b4",  # Blue (reused)
        "Antillean Creole": "#ff7f0e",  # Orange (reused)
        "Croatian": "#e377c2",  # Pink (reused)
        "Corsican": "#c49c94",  # Brown (reused)
        "Bosnian": "#f7b6d2",  # Pink (lighter)
        "Estonian": "#c7c7c7",  # Gray (lighter)
        "Hungarian": "#ff9896",  # Pink (lighter)
        "Lithuanian": "#98df8a",  # Green (lighter)
        "Polish": "#c5b0d5",  # Purple (lighter)
        "Romanian": "#ffbb78",  # Orange (lighter)
        "Russian": "#17becf",  # Cyan (reused)
        "Slovak": "#bcbd22",  # Olive (reused)
        "Vorarlbergish": "#1f77b4",  # Blue (reused)
        "Breton": "#ff7f0e",  # Orange (reused)
        "Macedonian": "#d62728",  # Red (reused)
        "Samogitian": "#9467bd",  # Purple (reused)
        "Serbian": "#8c564b",  # Brown (reused)
        "Imaginary": "#e377c2",  # Pink (reused)
        "Catalan": "#7f7f7f",  # Gray (reused)
        "Võro": "#bcbd22",  # Olive (reused)
        "Latvian": "#17becf",  # Cyan (reused)
        "Ukrainian": "#1f78b4",  # Blue (darker)
        "Montenegrin": "#ff9896",  # Pink (lighter)
        "Albanian": "#98df8a",  # Green (lighter)
        "Tahitian": "#c5b0d5",  # Purple (lighter)
        "Armenian": "#c49c94",  # Brown (lighter)
        "Bulgarian": "#f7b6d2",  # Pink (lighter)
        "Czech": "#c7c7c7",  # Gray (lighter)
        'English ("Franglais")': "#ffbb78",  # Orange (lighter)
        "Romani": "#2ca02c",  # Green (reused)
        "Swahili": "#d62728",  # Red (reused)
        "Georgian": "#9467bd",  # Purple (reused)
        "Udmurt": "#8c564b",  # Brown (reused)
        "Crimean Tatar": "#e377c2",  # Pink (reused)
        "Belarusian": "#7f7f7f",  # Gray (reused)
        "Srnan Tongo": "#bcbd22",  # Olive (reused)
        "Latin": "#17becf",  # Cyan (reused)
    }


def get_indicator_line_chart(
    filtered_data: pd.DataFrame, randomly_chosen_column: str, country: str
) -> alt.Chart:
    return (
        alt.Chart(filtered_data)
        .mark_line()
        .encode(
            x="Year:O",
            y=alt.Y(
                randomly_chosen_column.replace(":", r"\:"),
                title=f"{randomly_chosen_column}",
            ),
            color=alt.Color("Country Name:N", scale=alt.Scale(scheme="purples")),
            tooltip=["Country Name", "Year", randomly_chosen_column],
        )
        .properties(title=f"{randomly_chosen_column} by Year in {country}", width=1000)
    )


def get_eurovision_line_chart(filtered_data: pd.DataFrame, country: str) -> alt.Chart:
    return (
        alt.Chart(filtered_data)
        .mark_line()
        .encode(
            x="Year:O",
            y=alt.Y("Grand Final Place", scale=alt.Scale(reverse=True)),
            color=alt.Color("Country Name:N", scale=alt.Scale(scheme="magma")),
            tooltip=["Country Name", "Year", "Grand Final Place"],
        )
        .properties(title=f"{country} Eurovision Final Place", width=1000)
    )


def get_layered_chart(
    chart_one: alt.Chart,
    chart_two: alt.Chart,
    randomly_chosen_column: str,
    country: str,
) -> alt.Chart:
    return (
        alt.layer(chart_one, chart_two)
        .resolve_scale(y="independent", color="independent")
        .properties(
            title=f"{randomly_chosen_column} and Eurovision Place by Year in {country}",
            width=1000,
        )
    )


def filter_by_country(merged_df: pd.DataFrame, country_name: str) -> pd.DataFrame:
    return merged_df[merged_df["Country Name"].isin([country_name])]


def make_layer_chart(full_dataset: pd.DataFrame, country: str, randomly_chosen_column):
    country_data = filter_by_country(full_dataset, country)
    indicator = get_indicator_line_chart(country_data, randomly_chosen_column, country)
    eurovision = get_eurovision_line_chart(country_data, country)
    return get_layered_chart(indicator, eurovision, randomly_chosen_column, country)


def create_year_chart(year, data):
    COLORS = get_colors()
    filtered_data = data[data["Year"] == year]
    if filtered_data.empty:
        return f"No data for {year}"
    languages = filtered_data["Language"].unique()
    return (
        alt.Chart(filtered_data)
        .mark_bar()
        .encode(
            x=alt.X("Country", title="Country", sort="-y"),
            y=alt.Y("Grand Final Points", title="Total Grand Final Points"),
            color=alt.Color(
                "Language",
                scale=alt.Scale(
                    domain=list(COLORS.keys()), range=list(COLORS.values())
                ),
            ).legend(values=languages),
            tooltip=["Country", "Language", "Grand Final Points"],
        )
        .properties(title=f"Total Grand Final Points in {year}", width=1000)
    )


def make_count_chart(data: pd.DataFrame):
    colors = get_colors()
    return (
        alt.Chart(data)
        .mark_bar()
        .encode(
            y=alt.Y("count()", title="Number of Songs"),
            x=alt.X("Language", title="Language", sort="-y"),
            color=alt.Color(
                "Language",
                scale=alt.Scale(
                    domain=list(colors.keys()), range=list(colors.values())
                ),
            ).legend(None),
            tooltip=["Language", "count()"],
        )
        .properties(
            title="Total number of times a language is used in a song", width=1000
        )
    )


def make_points_chart(data):
    colors = get_colors()
    return (
        alt.Chart(data)
        .mark_bar()
        .encode(
            y=alt.Y("sum(Grand Final Points)", title="Sum of points won"),
            x=alt.X("Language", title="Language", sort="-y"),
            color=alt.Color(
                "Language",
                scale=alt.Scale(
                    domain=list(colors.keys()), range=list(colors.values())
                ),
            ).legend(None),
            tooltip=["Language", "sum(Grand Final Points)"],
        )
        .properties(title="Total points scored using x language", width=1000)
    )


def make_averages_chart(data):
    colors = get_colors()
    return (
        alt.Chart(data)
        .mark_bar()
        .encode(
            y=alt.Y("median(Grand Final Points)"),
            x=alt.X("Language", sort="-y"),
            tooltip=["Language", "median(Grand Final Points)"],
            color=alt.Color(
                "Language",
                scale=alt.Scale(
                    domain=list(colors.keys()), range=list(colors.values())
                ),
            ).legend(None),
        )
        .properties(title="Average points scored for songs in x language", width=1000)
    )
