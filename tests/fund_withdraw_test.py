from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def test_fund_withdraw():
    account = get_account()
    fundme = deploy_fund_me()
    entrance_fee = fundme.getEntranceFee()
    tx = fundme.fund({"from": account, "value": entrance_fee})
    tx.wait(1)

    assert fundme.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fundme.withdraw({"from": account})
    tx2.wait(1)
    assert fundme.addressToAmountFunded(account.address) == 0
