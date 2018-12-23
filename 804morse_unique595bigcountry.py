def uniqueMorseRepresentations(words):
    morse_lst = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.","---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alpha_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result_set = set()
    #根据上面的一一对应的表得到唯一的集合，其实也可以用字典
    for word in words:
        result_str = ''
        for i in word:
            result_str += morse_lst[alpha_lst.index(i)]
        result_set.add(result_str)
    return len(result_set)


def uniqueMorseRepresentations2(words):
    morse_lst = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.","---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alpha_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    morse_alpha_dict= dict(zip(alpha_lst, morse_lst))
    result_set = set()
    #用字典
    for word in words:
        result_str = ''
        for i in word:
            result_str += morse_alpha_dict[i]
        result_set.add(result_str)
    return len(result_set)

#595 big country:
#Write your MySQL query statement below
#select name,population,area from World where area > 3000000 or population > 25000000;

if __name__ == '__main__':
    word_lst = ["gin", "zen", "gig", "msg"]
    print(uniqueMorseRepresentations2(word_lst))
