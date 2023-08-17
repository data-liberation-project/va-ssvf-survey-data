from typing import Iterator, Optional

import pdfplumber
import polars as pl


def get_page_table_rows(page: pdfplumber.page.Page) -> list[list[Optional[str]]]:
    tables = page.extract_tables()
    return tables[0] if tables else []


def get_all_table_rows(
    pdf: pdfplumber.pdf.PDF, page_indices: list[int]
) -> Iterator[list[Optional[str]]]:
    for page_ix in page_indices:
        page = pdf.pages[page_ix]
        rows = get_page_table_rows(page)
        yield from rows


COLUMNS = [
    "grant_id",
    "provider_name",
    "responses_total",
    "responses_top_2",
    "performance_rating",
]


def main() -> None:
    pdf = pdfplumber.open("pdfs/VA SSVF Year End Report FY20.pdf")
    page_ixs = [20, 21, 22, 23, 24]
    rows = list(get_all_table_rows(pdf, page_ixs))

    (
        pl.DataFrame(rows[1:], schema=COLUMNS)
        .filter(pl.col("grant_id") != "Grant ID")
        .with_columns(pl.col("performance_rating").str.strip("%").cast(float))
        .write_csv("data/from-pdfs/provider-satisfaction-fy20.csv")
    )


if __name__ == "__main__":
    main()
