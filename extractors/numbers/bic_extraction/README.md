The module extracts the BIC from a given text. BIC (Bank Identifier Code) is the international standard for the bank sort code constracted as follows: The BIC is in total 8 or 11 characters long. The first 4 characters are letters and contain the ID of the bank, the following 2 are alphabetical and mark the country. The first of these characters is not allowed to be 0 or 1. Next, there are 2 alphanumerical characters to code the location. Finally there can be 3 alphanumerical characters for characterizing the branch (optional). There are alphanumerical, but if the first character is an X, the next two characters have to be X's, too. 