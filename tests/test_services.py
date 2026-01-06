from src.services import investment_bank


def test_investment_bank(test_sample_data):
    trans_load = test_sample_data.to_dict('records')
    inv_kop = investment_bank("2020-01", trans_load, 50)
    assert inv_kop == 21.95
