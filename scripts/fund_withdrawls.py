from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund_withdrawls_deploy():
    fundme = FundMe[-1]
    account = get_account()
    entrance_fee = fundme.getEntranceFee()
    print(entrance_fee)
    fundme.fund({"from": account, "value": entrance_fee})


def wuthdraw():
    fundme = FundMe[-1]
    account = get_account()
    fundme.withdraw({"from": account})


def main():
    fund_withdrawls_deploy()
    wuthdraw()
