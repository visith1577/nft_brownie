from scripts.helpful_script import LOCAL_BLOCKCHAIN_NETWORK, get_account
from scripts import deploy
from brownie import network
import pytest


def test_simple_collectible():
    if network.show_active() in LOCAL_BLOCKCHAIN_NETWORK:
        pytest.skip()
    simple_collectible = deploy.main()
    assert simple_collectible.ownerOf(0) == get_account()