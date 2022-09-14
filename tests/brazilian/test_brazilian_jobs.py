from src.brazilian_jobs import read_brazilian_file

mock_result = {
    "title": "Analista de Software",
    "salary": "4000",
    "type": "full time",
}
path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    assert mock_result in read_brazilian_file(path)
