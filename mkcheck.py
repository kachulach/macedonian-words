#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

# Input: text via STDIN
# Output: list of errors

text = u"""Како еден од првите новинраи кои ги објавија доверливите документи што дека американската NSA ги шпионира сите – од обичните интернет корисници до лидерите на западните земји; добитникот на Пулицеровата награда, Глен Гринвалд, знае дека приватноста е клучно човеково право кое мора да си го заштитиме.

Во својот TED говор, г. Гринвалд зборува за реакциите на луѓето што ги забележал по објавувањето на тајните документи на NSA. Нема воопшто да ве изненади дека овој говор кој е објавен во октомври лани, може многу лесно да се примени и на прислушувањето во Македонија што беше обелоденето со таканаречената „бомба“. Македонските власти неовластено прислушуваат над 20.000 луѓе, и иако ова треба да биде фокусот на дебатите, луѓето сепак зборуваат дека нема што да кријат. Напротив, вели г. Гринвалд.

„Има причина зошто сакаме приватнсот, и таа причина е дека сите ние- не само терористите и криминалците – туку сите ние имаме потреба да се скриеме“, вели тој во својот TED говор. „Човечката срам е моќен мотиватор, и желбата да ја избегнеме, е причината зошто луѓето кога се во состојба да знаат дека се набљудувани, прават одлуки кои не се продукт на нивното однесување, туку очекувањата што другите ги имаат за нив или нормите во друштвеното опкружување“.
"""

lines = codecs.open('MK-dict.txt', 'r', 'utf-8').readlines()

DICT = {}
for l in lines:
    DICT[l.replace('\r\n', '')] = 1

def is_cyrillic_letter(letter):
    letters = u"љњертѕуиопасдфгхјклзџцвбнмЉЊЕРТЅУИОПАСДФГХЈКЛЗЏЦВБНМчЧќЌѓЃшШ"
    return letter in letters

def is_cyrillic_word(word):
    return all(map(is_cyrillic_letter, word))

def words_with_positions(text):
    words = []
    current_word = ''
    inside_word = False
    word_start = 0
    for i, letter in enumerate(text):
        if is_cyrillic_letter(letter) and not inside_word:
            inside_word = True
            word_start = i
        if inside_word:
            if letter != ' ' and letter != '\n':
                current_word += letter
        if letter == ' ' or letter == '\n' and inside_word:
            w = (current_word, word_start, i)
            words.append(w)
            inside_word = False
            current_word = ''
    if inside_word:
        w = (current_word, word_start, i)
        words.append(w)
    return words

def replace_some_symbols(word):
    return word.replace('.', '') \
               .replace(',', '') \
               .replace(';', '') \
               .replace(u'„', '') \
               .replace(u'“', '') \
               .replace('-', '')

for w in words_with_positions(text):
    word, start, end = w
    if word in DICT:
        continue
    else:
        clean_word = replace_some_symbols(word)
        if clean_word.lower() not in DICT:
            sys.stdout.write(w[0])
            sys.stdout.write(' ' + str(w[1]))
            sys.stdout.write(' ' + str(w[2]))
            sys.stdout.write('\n')

def strip_non_cyrillic(word):
    pass

def check(text):
    words = text.split(' ')
    for word in words:
        sys.stdout.write(word)
        sys.stdout.write('\n')

# check(text)