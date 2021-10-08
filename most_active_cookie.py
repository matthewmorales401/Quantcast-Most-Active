#!/usr/bin/env python
from collections import defaultdict
import unittest
import sys

#Define function that will check for most active cookie
def mostActiveCookie(inputDate, f):

    #Check if valid file name
    try:
        f = open(f, "r")
    except:
        return "Input valid file name and/or date"

    #Create hash map that stores counts of cookies through other hash maps.
    cookieMap = defaultdict(dict)
    maximumCookie = []
    for cookieLine in f.readlines():
        cookieLine = cookieLine.strip('\n').split(',')
        cookie = cookieLine[0]
        date = cookieLine[1].split('T')[0]
        if cookie != 'cookie':
            if cookie in cookieMap[date]:
                cookieMap[date][cookie] += 1
            else:
                cookieMap[date][cookie] = 1
    #close file
    f.close()

    #Find most active cookie(s) through the hash map values.
    
    for cookie in cookieMap[inputDate]:
        if not maximumCookie:
            maximumCookie.append(cookie)
        elif cookieMap[inputDate][cookie] > cookieMap[inputDate][maximumCookie[0]]:
            maximumCookie = [cookie]
        elif cookieMap[inputDate][cookie] == cookieMap[inputDate][maximumCookie[0]]:
            maximumCookie.append(cookie)

    #print cookies that appeared the most at specified date
    if maximumCookie:
        for i in maximumCookie:
            print(i)
        return maximumCookie
    else:
        return 'There are no cookies for that specified date'

#Main function. Check edge cases for invalid arguments. Otherwise, run code as expected.
def main():
    if len(sys.argv) != 4:
        print("There should be only 3 arguments")
    elif sys.argv[2] != "-d":
        print("Third argument must be -d")
    else:
        mostActiveCookie(sys.argv[3], sys.argv[1])
    input('Press Enter to exit')

#Unit tests/edge cases
class TestActive(unittest.TestCase):
    def test_example1(self):
        mostActive = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
        f = 'cookie_log.csv'
        self.assertEqual(mostActiveCookie('2018-12-08', f), mostActive, "Wrong cookies.")

    def test_example2(self):
        mostActive = ['AtY0laUfhglK3lC7']
        f = 'cookie_log.csv'
        self.assertEqual(mostActiveCookie('2018-12-09', f), mostActive, "Wrong cookies.")

    def test_example3(self):
        errorMessage = 'There are no cookies for that specified date'
        f = 'cookie_log.csv'
        self.assertEqual(mostActiveCookie('2011-12-01', f), errorMessage, "There should be no cookies.")

    def test_example4(self):
        errorMessage = "Input valid file name and/or date"
        f = 'dummylog.csv'
        self.assertEqual(mostActiveCookie('2011-12-01', f), errorMessage, "The file should be invalid.")

    def test_example5(self):
        argumentLength = 4
        self.assertEqual(argumentLength, 4, "There should be only 4 arguments.")

#main for unit testing
if __name__ == '__main__':
    main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
