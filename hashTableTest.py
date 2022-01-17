from hashtable import HashTable
import pytest

#basic cases
def test_add():
    table = HashTable()
    table.add(100, "Hello")
    table.add(1100, "Hi")
    assert table.lst[table.hash_function(100)] == (100, "Hello")
    assert table.lst[table.hash_function(1100)+1] == (1100, "Hi")

def test_get():
    table = HashTable()
    table.add(100, "Hello")
    assert table.get(100) == "Hello"

def test_delete():
    table = HashTable()
    table.add(100, "Hello")
    table.delete(100)
    assert table.lst[table.hash_function(100)] == None

# wrap cases

def test_add_wrap():
    table = HashTable()
    key1 = 581
    key2 = 1581
    table.add(key1, "Hello")
    table.add(key2, "Hi")
    assert table.lst[999] == (key1, "Hello")
    assert table.lst[0] == (key2, "Hi")

def test_get_wrap():
    table = HashTable()
    key1 = 581
    key2 = 1581
    table.add(key1, "Hello")
    table.add(key2, "Hi")

    assert table.get(key1) == "Hello"
    assert table.get(key2) == "Hi"

def test_delete_wrap():
    table = HashTable()
    key1 = 581
    key2 = 1581
    table.add(key1, "Hello")
    table.add(key2, "Hi")
    table.delete(key2)

    assert table.get(key1) == "Hello"
    assert table.get(key2) == None