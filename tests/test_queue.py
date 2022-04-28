import pytest
import xdoctest

from demo import QueueBuiltByTwoStacks


def test_stack():
    # the docstring example in QueueBuiltByTwoStacksWangwenjun.__repr__
    xdoctest.doctest_callable(QueueBuiltByTwoStacks.__repr__)
    #  the docstring example in QueueBuiltByTwoStacksWangwenjun.__len__
    xdoctest.doctest_callable(QueueBuiltByTwoStacks.__len__)
    queue = QueueBuiltByTwoStacks()
    queue.put(1)
    queue.put(2)

    assert repr(queue) == 'queue of length 2'
    assert len(queue) == 2
    assert not queue.empty()
    assert 1 == queue.get()
    assert 2 == queue.get()
    assert queue.empty()
    with pytest.raises(AssertionError):
        queue.get()
