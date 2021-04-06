import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_newest_by_category():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=1.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest_by_category("Clothing")

    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(1.0)


def test_newest_by_category_no_matches_is_none():
    item_a = Decor(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = tai.get_newest_by_category("Electronics")

    assert newest_item is None


def test_newest_by_category_with_duplicates():
    item_a = Clothing(age=2.0)
    item_b = Clothing(age=2.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = tai.get_newest_by_category("Clothing")

    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(2.0)


def test_swap_by_newest_item():
    item_a = Clothing(age=2.0)
    item_b = Electronics(age=7.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=1.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=6.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest_item(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert result is True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_e not in jesse.inventory
    assert item_f in jesse.inventory


def test_swap_by_newest_item_if_my_inventory_empty():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest_item(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert result is False
    assert len(tai.inventory) is 0
    assert len(jesse.inventory) is 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_by_newest_item_if_their_inventory_empty():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest_item(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert result is False
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory