#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

print("---------")
text_indentation("""sentence one. sentence two.""")
print("---------")
text_indentation("""1.         2?       3:           4.       5?          6:   7.""")
print("---------")
text_indentation("""sentence one""")
print("---------")
text_indentation("""sentence one.sentence two""")
print("---------")
text_indentation("Holberton School")
print("---------")
print("no end", end="")
print("nextline")
