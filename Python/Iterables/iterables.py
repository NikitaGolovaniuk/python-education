import re


class SentenceIterator:
    def __init__(self, text):
        self.index = 0
        self.text = text

    def __next__(self):
        try:
            text = self.text[self.index]
        except IndexError:
            raise StopIteration()
        self.index = self.index + 1
        return text


class MultipleSentencesError(Exception):
    pass


class Sentence:
    def __init__(self, text: str):
        if not re.findall("[0-9]", text):  # isinstance(text, str):
            if not re.findall("[.?!]$", text):
                raise ValueError
            if len(re.findall(r'[.!?]', text)) >= 2:
                raise MultipleSentencesError
            self.text = text
        else:
            raise TypeError

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def __getitem__(self, item):
        return self.words[item]

    def _words(self):
        print(self.text)
        print(re.findall(r'\w+', self.text))
        for words in re.findall(r'\w+', self.text):
            yield words

    #
    @property
    def words(self):
        return re.findall(r'\w+', self.text)

    @property
    def other_chars(self):
        return re.findall('[^a-zA-Z]', self.text)


# # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# #  TypeError
# a = Sentence(123)
# #  ValueError
# a = Sentence('Im Nebel ruhet noch die Welt')
# # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# # пример работы: __repr__() >>> <Sentence(words=13, other_chars=7)>
# a = Sentence("Noch träumen Wald und Wiesen: Bald siehst du, wenn der Schleier fällt, "
#              "Den blauen Himmel unverstellt, Herbstkräftig die gedämpfte Welt In warmem Golde fließen.")
# print(repr(a))
# # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# # метод Sentence()._words должен возвращать ленивый итератор
# a = Sentence("Der Abend, der sich in die Nacht verblutet,Rührt deine Seele stets mit gleicher Frage, "
#              "Denn täglich wehst du mit dem toten Tage Ins Dunkel weiter, das die Welt umflutet.")
# print(a._words())
# wunder_gen = a._words()
# print(next(wunder_gen))
# print(next(wunder_gen))
# # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# # имеет свойство Sentence().words , которое возвращает список всех слов в
# # предложении (*напоминаю, что мы не хотим хранить все эти слова в
# # нашем объекте)
# a = Sentence("nd jedes ist zu neuen Wundern Welle.")
# print(a.words)
# # имеет свойство Sentence().other_chars , которое возвращает список всех не
# # слов в предложении
# print(a.other_chars)
# # умеет отдавать слово по индексу
# # пример работы: Sentence('Hello world!')[0] >>> 'Hello'
# print(a[0])
# # умеет отдавать срез по словам
# # пример работы: Sentence('Hello world!')[:] >>> 'Hello world'
# print(a[0:3])
# # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# # может быть использован в цикле for:
# a = Sentence("Und fast schon nahe jenem letzten Strand.")
# for word in a:
#     print(word)
# # -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

