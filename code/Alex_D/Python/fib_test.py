import unit_converter_1;
from io import StringIO;

def test_unit_converter_1(monkeypatch):
    number_inputs = StringIO('12\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert unit_converter_1.unit_converter() == "12 ft is 3.6576000000000004 m"