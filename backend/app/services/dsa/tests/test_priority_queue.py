import pytest

from app.services.dsa.priority_queue import PriorityQueue


def test_priority_queue_push_and_pop():
    queue = PriorityQueue()

    queue.push(5, "A")
    queue.push(2, "B")
    queue.push(8, "C")
    queue.push(1, "D")

    assert queue.pop() == (1, "D")
    assert queue.pop() == (2, "B")
    assert queue.pop() == (5, "A")
    assert queue.pop() == (8, "C")


def test_priority_queue_peek():
    queue = PriorityQueue()

    queue.push(5, "A")
    queue.push(2, "B")

    assert queue.peek() == (2, "B")
    assert queue.peek() == (2, "B")


def test_priority_queue_is_empty():
    queue = PriorityQueue()

    assert queue.is_empty()

    queue.push(1, "A")

    assert not queue.is_empty()

    queue.pop()

    assert queue.is_empty()


def test_pop_empty_queue():
    queue = PriorityQueue()

    with pytest.raises(IndexError):
        queue.pop()


def test_peek_empty_queue():
    queue = PriorityQueue()

    with pytest.raises(IndexError):
        queue.peek()