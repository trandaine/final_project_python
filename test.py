from library_item import LibraryItem
import pytest

def test_valid_input():
    item = LibraryItem("Movie Name", "Director Name",4, ".\\image\\image.jpg")
    assert item.name == "Movie Name"
    assert item.director == "Director Name"
    assert item.rating == 4
    assert item.play_count == 0
    assert item.img == ".\\image\\image.jpg"

def test_invalid_rating():
    with pytest.raises(ValueError):
        LibraryItem("Movie Name", "Director Name", ".\\image\\image.jpg", 6)

def test_invalid_name_type():
    with pytest.raises(TypeError):
        LibraryItem(123, "Director Name",4, ".\\image\\image.jpg")