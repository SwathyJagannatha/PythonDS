class Solution:

    #Function to check if a string is Pangram or not.
    def checkPangram(self, s):

        #using a hash table to mark the characters present in the string.
        marked = [0 for i in range(26)]

        #iterating over the string.
        for char in s:

            #marking index of current character as true in hash table.

            #if we get uppercase character, we subtract 'A' from it
            #to get its index (in terms of 0 to 25).
            if (ord(char) <= ord('Z') and ord(char) >= ord('A')):
                marked[ord(char) - ord('A')] = 1

            #if we get lowercase character, we subtract 'a' from it
            #to get its index (in terms of 0 to 25).
            elif (ord(char) <= ord('z') and ord(char) >= ord('a')):
                marked[ord(char) - ord('a')] = 1

        #returning false if any letter of alphabet is unmarked.
        for i in range(26):
            if (not marked[i]):
                return False

        #if all letters of alphabet are present then returning true.
        return True