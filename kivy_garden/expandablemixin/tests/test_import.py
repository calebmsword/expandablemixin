import pytest


def test_flower():
    from kivy_garden.expandablemixin import FlowerLabel
    label = FlowerLabel()
    assert label.text == 'Demo expandablemixin'
