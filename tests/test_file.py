# coding=utf-8
import os
TEST_DIR = os.path.dirname(os.path.realpath(__file__))


def test_return_carriages():
    with open(os.path.join(TEST_DIR, 'sample.txt'), encoding='latin-1', newline='') as sample_text:
        assert "\r\n" in sample_text.read()
