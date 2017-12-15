################################################################################
# Gozde DOGAN
# 131044019
# CSE321 - Introduction to Algorithm Design
# Homework 4
# Question 2
################################################################################

################################################################################
#
# Metodlarin uzerinde yorum bloklari icinde neler yaptiklari ve karmasikliklari 
# ayrintili olarak anlatildi.
# longest_common_postfix metodunun karmasikligi logk+(x*y*m*n) olarak bulundu.
# Tasarlanan algoritmanin karmasikligi logk+(x*y*m*n)'dir.
#
################################################################################

import sys

def main():
################################################################################
    print "\n"
    inpStrings = ["absorptivity", "circularity", "electricity", "importunity", "humanity"]
    lcp = longest_common_postfix(inpStrings)
    print(inpStrings)
    print(lcp)
    print "\n"
    
################################################################################
#    inpStrings1 = ["bash", "trash", "backslash", "flash"]
#    lcp = longest_common_postfix(inpStrings1)
#    print(inpStrings1)
#    print(lcp)
#    print "\n"

################################################################################
#    inpStrings2 = ["gozde", "ozlem", "soz"]
#    lcp = longest_common_postfix(inpStrings2)
#    print(inpStrings2)
#    print(lcp)
#    print "\n\n"


################################################################################ 
#
# inputStrings'in boyutu k olarak dusunulurse;
# Best case'i k'nin 1 veya 0 olmasi durumu, lineer zaman
# Worst case'i liste her seferinde 2ye bolunerek ilerleniyor, her levelde k/2^x 
# seklinde bolunmus listenin eleman sayisi ifadesi karsimiza cikiyor.
# Bunun ayni sira birde findSubString metodu cagriliyor;
# findSubString metodunun karmasikligi; 
# Burdan da worst case logk+(x*y*m*n) olarak bulunur. 
#
################################################################################ 
def longest_common_postfix(inpStrings):
    if len(inpStrings) == 0:
        return None
    elif len(inpStrings) == 1:
        return inpStrings[0]
    else:
        middle = len(inpStrings)/2
        LeftPart = inpStrings[0:middle]
        RightPart = inpStrings[middle:len(inpStrings)]
        
        left_lcp = longest_common_postfix(LeftPart)
        right_lcp = longest_common_postfix(RightPart)
        
        if cmp(left_lcp, right_lcp) == 0:
            return left_lcp
        else:
            return findSubString(left_lcp, right_lcp)


################################################################################ 
#
# Liste icinden gelen stringlerin alt stringlerini bulmaya calisiyor. 
# Buldugu substringleri return ediyor.
#
# findSubSubString metodunun worst case'i m*n, best case'i constant zaman.
# findSubString metodu for donguleri best case'de de worst case'de de doner;
# donme sayisi (x/2)*(y/2)= x*y'dir. (left boyutu x, right boyutu y gibi dusunuldu)
# findSubString metodunun karmasikligi best ve worst casede esittir,
# ve x*y*m*n'dir.
#
################################################################################ 
def findSubString(left, right):
    subStr = ""
    subStrArr = []
    
    for i in range(0, len(left)):
        for j in range(0, len(right)):
            if left[i] == right[j]:
                #print "left:", left[i:], "\tright:", right[j:]
                leftleft = left[i:]
                rightright = right[j:]
                subStr = findSubSubString(leftleft, rightright)
                subStrArr.append(subStr)

    maxStrLen = 0
    maxStrIndex = -1
    for i in range(0, len(subStrArr)):
        if maxStrLen < len(subStrArr[i]):
            maxStrLen = len(subStrArr[i])
            maxStrIndex = i            
    
    if maxStrIndex == -1:
        return None
    else:
        return subStrArr[maxStrIndex]

################################################################################ 
# Bu metot gelen stringler icinde sirali bir sekilde ilerlerken art arda esit 
# olan karakter sayisini bulur, yani iki stringin sub stringi bulunur ve return 
# edilir.
#
# str1, boyut=m
# str2, boyut=n
# m >= n
# Worst Case de iki dongu de sonuna kadar dolasilir (iki string birbirine esit)
# Worst Case m*n zamandir.
# Best Case de ikinci karakterler esit olmaz 
# (ilk karakterer esit oldugu icin bu metot calisti) 
# Bu durumda da Best Case sabit zamandir.
################################################################################ 
def findSubSubString(str1, str2):
    subString = ""
    result = 0
    #print "str1:", str1, "\tstr2:", str2
    #print "lenstr1:", len(str1), "\tlenstr2:", len(str2)
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            #print "i:", i, "\tstr1[i]:", str1[i], "\tj:", j, "str2[j]:", str2[j] 
            if str1[i] == str2[j]:
                subString = subString + str1[i]
                i += 1
                j += 1
            else:
                result = 1
                break
                
        if result == 1:
            break
            
    return subString
            
            
                
if __name__ == "__main__":
    main()
    
