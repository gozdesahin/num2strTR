__author__ = 'Periphery'
# -*- coding: utf-8 -*-
import re

# unicode characters!
nums = {0: u'sıfır', 1: u'bir', 2: u'iki', 3: u'üç', 4: u'dört', 5: u'beş', 6: u'altı', 7: u'yedi', 8: u'sekiz', 9: u'dokuz',
           10: u'on',20: u'yirmi', 30: u'otuz', 40: u'kırk', 50: u'elli', 60: u'altmış', 70: u'yetmiş', 80: u'seksen',
           90: u'doksan', 100: u'yüz', 1000: u'bin', 1000000: u'milyon', 1000000000: u'milyar', 1000000000: u'trilyon'}

"""
Verilen sayının Türkçe okunuşunu döndürür. Negatif sayılar, ondalık sayılar, üslü sayıları kapsamamaktadır. Yalnızca
tam sayılar için çalışır. Örnek kullanım aşağıda verilmiştir
--------------------------------------------------------------------------------------------------------------------
It returns the pronunciation of the given integer number in Turkish. It only works for positive integers, not for
floating, negative or exponential numbers. Check out the test part for usage information
"""

def is_integer(s):
  return re.search("[^0-9]", s) is None

def  num2str(str_num):
    """
    :rtype : string
    :param number: unicode character array
    :return: If it's an integer, it returns the pronunciation, otherwise input is returned
             Eğer bir sayıysa Türkçe okunuşunu döndürür, değilse kendini döndürür
    """
    l = ''
    # öncelikle sayı mı kontrolü
    if is_integer(str_num):
        basamak = len(str_num)
        j = -1
        for i in range(basamak-1,-1 ,-1):
            index = basamak-i-1
            # 1'ler (4'ler, 7'ler) basamağını yazar
            if (index%3)==0:
                j+=1
                rev_str = str_num[::-1]
                # gerektiğinde bin, milyon, milyar vs... yazar (1000000: bir milyon bin yazmaması için)
                if (j!=0) and (int(rev_str[(j*3):(3*(j+1))])>0):
                    if (1000**j) in nums:
                        l = nums[1000**j]+u' '+l
                    else:
                        return str_num
                # sadece tek basamaklı sıfır için
                if (index==0) and (basamak==1):
                    l = nums[int(str_num[i])]+u' '+l
                # milyon,bin vs... nin önündeki rakamı ekler (2 milyon)
                elif (int(str_num[i])!= 0) and ((basamak>4) or (index==0)):
                    l = nums[int(str_num[i])]+u' '+l
            # 10'lar (2'ler, 5'ler, 8'ler vs...) basamağını yazar
            elif (index%3)==1:
                if (int(str_num[i])!=0):
                    l = nums[int(str_num[i])*10]+u' '+l
            # 100'ler (3'ler, 6,9 vs..) basamağını yazar
            elif (index%3)==2:
                if (int(str_num[i])!= 1) and (int(str_num[i])!= 0):
                    l = nums[int(str_num[i])]+u' yüz'+u' '+l
                elif(int(str_num[i])!= 0):
                    l = u'yüz'+u' '+l
        return ''.join(l)
    else:
        # print u"Bu bir sayı değil"
        return str_num


# Test : Usage examples
print num2str('0')
print num2str('10')
print num2str('252')
print num2str('1052')
print num2str('89962')
print num2str('1000000')
print num2str('1025478')
print num2str('1000000000')
print num2str('1003004005')
print num2str(str(1003004005))
print num2str(u'abc')
