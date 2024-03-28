import pytest

from main import check_resource


def test1():
    assert check_resource("tests/testFiles/testFile1.txt") == "Input not in .json file format"


def test2():
    assert check_resource("tests/testFiles/testFile2.json") == "Input not in AWS::IAM::Role Policy format"

def test3():
    assert check_resource("tests/testFiles/testFile3.json") == "Input not in AWS::IAM::Role Policy format"


def test4():
    assert check_resource("tests/testFiles/testFile4.json") == "Input not in AWS::IAM::Role Policy format"

def test5():
    assert check_resource("tests/testFiles/testFile5.json") == "Input not in AWS::IAM::Role Policy format"

def test6():
    assert check_resource("tests/testFiles/testFile6.json") == "Input not in AWS::IAM::Role Policy format"

def test7():
    assert check_resource("tests/testFiles/testFile7.json") == "Input not in AWS::IAM::Role Policy format"

def test8():
    assert check_resource("tests/testFiles/testFile8.json") == "Input not in AWS::IAM::Role Policy format"

def test9():
    assert check_resource("tests/testFiles/testFile9.json") == "Input not in AWS::IAM::Role Policy format"

def test10():
    assert check_resource("tests/testFiles/testFile10.json") == "Input not in AWS::IAM::Role Policy format"

def test11():
    assert check_resource("tests/testFiles/testFile11.json") == "Input not in AWS::IAM::Role Policy format"

def test12():
    assert check_resource("tests/testFiles/testFile12.json") == "Input not in AWS::IAM::Role Policy format"

def test13():
    assert check_resource("tests/testFiles/testFile13.json") == "Input not in AWS::IAM::Role Policy format"

def test14():
    assert check_resource("tests/testFiles/testFile14.json") == "Input not in AWS::IAM::Role Policy format"

def test15():
    assert check_resource("tests/testFiles/testFile15.json") == "Input not in AWS::IAM::Role Policy format"

def test16():
    assert check_resource("tests/testFiles/testFile16.json") == "Input not in AWS::IAM::Role Policy format"

def test17():
    assert check_resource("tests/testFiles/testFile17.json") == True

def test18():
    assert check_resource("tests/testFiles/testFile18.json") == False

def test19():
    assert check_resource("tests/testFiles/testFile19.json") == True




