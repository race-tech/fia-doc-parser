from contextlib import nullcontext
import json

import pytest

from fia_doc_parser.parser import EntryListParser

race_list = [
    (
        2025,
        1,
        nullcontext()
    ),
    (
        # Two and only two reserve drivers (#55)
        2025,
        9,
        pytest.warns(UserWarning, match='Error when parsing driver')
    )
]
# Not going to test year 2023 for entry list, as the PDF format changed, and we are not interested
# in retrospectively parsing old entry list PDFs


@pytest.fixture(params=race_list)
def prepare_entry_list_data(request) -> tuple[list[dict], list[dict]]:
    # Download and parse entry list PDF
    year, round_no, context = request.param
    file_name = f'{year}_{round_no}_entry_list'

    with context:
        parser = EntryListParser('tests/fixtures/' + file_name + '.pdf', year, round_no)
        data = parser.df.to_json()

    # Sort by car No. for both json for easier comparison
    with open('tests/fixtures/' + file_name + '.json', encoding='utf-8') as f:
        expected_data = json.load(f)
    data.sort(key=lambda x: x['objects'][0]['car_number'])
    expected_data.sort(key=lambda x: x['objects'][0]['car_number'])
    return data, expected_data


def test_parse_entry_list(prepare_entry_list_data):
    data, expected_data = prepare_entry_list_data
    assert data == expected_data
