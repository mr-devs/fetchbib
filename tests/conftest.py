"""Shared test data and fixtures."""

# Sample DOIs for testing.
DOI_A = "10.1073/pnas.2322823121"
DOI_B = "10.1609/icwsm.v5i1.14126"
DOI_URL_A = f"https://doi.org/{DOI_A}"

# Search query that resolves to DOI_A
SEARCH_QUERY_A = "DeVerna Fact-checking information from large language models"

# Expected author in DOI_A results
AUTHOR_A = "DeVerna"

# Sample raw BibTeX for mocked tests (unformatted).
RAW_BIBTEX_A = "@article{Key1,author={Alice},year={2020}}"
RAW_BIBTEX_B = "@article{Key2,author={Bob},year={2021}}"

# Formatter test data: raw inputs and expected outputs.
FORMATTER_RAW_SINGLE_LINE = (
    "@article{DeVerna_2024,"
    "author={DeVerna, Matthew R. and Yan, Harry Yaojun and Yang, Kai-Cheng and Menczer, Filippo},"
    "doi={10.1073/pnas.2322823121},"
    "issn={1091-6490},"
    "journal={Proceedings of the National Academy of Sciences},"
    "month=dec,"
    "number={50},"
    "publisher={Proceedings of the National Academy of Sciences},"
    "title={Fact-checking information from large language models can decrease headline discernment},"
    "url={http://dx.doi.org/10.1073/pnas.2322823121},"
    "volume={121},"
    "year={2024}}"
)
FORMATTER_EXPECTED_SINGLE_LINE = (
    "@article{DeVerna_2024,\n"
    "  author = {DeVerna, Matthew R. and Yan, Harry Yaojun and Yang, Kai-Cheng and Menczer, Filippo},\n"
    "  doi = {10.1073/pnas.2322823121},\n"
    "  issn = {1091-6490},\n"
    "  journal = {Proceedings of the National Academy of Sciences},\n"
    "  month = dec,\n"
    "  number = {50},\n"
    "  publisher = {Proceedings of the National Academy of Sciences},\n"
    "  title = {Fact-checking information from large language models can decrease headline discernment},\n"
    "  url = {http://dx.doi.org/10.1073/pnas.2322823121},\n"
    "  volume = {121},\n"
    "  year = {2024}\n"
    "}"
)

# Uses DeVerna entry to test that commas in author names are preserved.
FORMATTER_RAW_AUTHOR_COMMAS = (
    "@article{DeVerna_2024,"
    "author={DeVerna, Matthew R. and Yan, Harry Yaojun and Yang, Kai-Cheng and Menczer, Filippo},"
    "title={Fact-checking},"
    "year={2024}}"
)

FORMATTER_RAW_TRAILING_COMMA = "@article{Key2020,author={Someone},year={2020},}"

FORMATTER_RAW_NESTED_BRACES = (
    "@inproceedings{Key2021,"
    "title={A {GPU}-Accelerated Approach},"
    "author={Smith, John},"
    "year={2021}}"
)
