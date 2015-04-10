It returns the pronunciation of the given integer number in Turkish. Currently, it only supports integers. I hope to extend this tool for floating, negative, exponential and ordered numbers. Check out the test part in num2string.py for usage information
Ex:
print num2str('0')  -> sıfır
print num2str('10') -> on
print num2str('252') -> iki yüz elli iki
print num2str('1052') -> bin elli iki 
print num2str('89962') -> seksen dokuz bin dokuz yüz altmış iki
print num2str('1000000') -> bir milyon 
print num2str('1025478') -> bir milyon yirmi beş bin dört yüz yetmiş sekiz 
print num2str('1000000000') -> bir trilyon 
print num2str('1003004005') -> bir trilyon üç milyon dört bin beş
print num2str(str(1003004005)) -> bir trilyon üç milyon dört bin beş
print num2str(u'abc') -> abc

P.S: Please note that the returned value will be a set of unicode characters
Written with Python 2.7 and tested on Windows 7 64bit