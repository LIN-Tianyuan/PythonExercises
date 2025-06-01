"""
English:
In English, the present participle is formed by adding the suffix -ing
to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)

If the verb ends in ie, change ie to y and add ing

For words consisting of consonant-vowel-consonant, double the final letter before adding ing

By default just add ing

Your task in this exercise is to define a function make_ing_form()
which given a verb in infinitive form returns its present participle form.
Test your function with words such as lie, see, move and hug.
However, you must not expect such simple rules to work for all cases.

Français:
En anglais, le participe présent se forme en ajoutant le suffixe -ing à la forme infinie : go -> going.
Un ensemble simple de règles heuristiques peut être donné comme suit :
Si le verbe se termine par e, laisser tomber le e et ajouter ing (sauf exception : be, see, flee, knee, etc.)

Si le verbe se termine par ie, remplacer ie par y et ajouter ing.

Pour les mots composés d'une consonne-voyelle-consonne, doubler la lettre finale avant d'ajouter ing.

Par défaut, il suffit d'ajouter ing

Votre tâche dans cet exercice est de définir une fonction make_ing_form() qui,
étant donné un verbe à la forme infinitive, retourne sa forme de participe présent.
Testez votre fonction avec des mots tels que lie, see, move et hug.
Cependant, vous ne devez pas vous attendre à ce que des règles aussi simples fonctionnent dans tous les cas.

中文：
在英语中，现在分词是通过在不定式上添加后缀 -ing 构成的：go -> going。
下面是一套简单的启发式规则：
如果动词以 e 结尾，去掉 e，加上 ing（如果不是例外情况：be、see、fleat、knee 等）。

如果动词以 ie 结尾，将 ie 改为 y 并加上 ing

对于由辅音-元音-辅音组成的单词，在添加 ing 前将最后一个字母加倍

默认情况下只需加上 ing

本练习的任务是定义一个函数 make_ing_form()，
在给定动词不定式的情况下，返回其现在分词形式。
请使用 lie、see、move 和 hug 等单词测试您的函数。
但是，您不能指望这种简单的规则适用于所有情况。
"""
def make_ing_form(verb):
    vowels = 'aeiou'
    exceptions = {'be', 'see', 'flee', 'knee'}

    if verb in exceptions:
        return verb + 'ing'
    elif verb.endswith('ie'):
        return verb[:-2] + 'ying'
    elif verb.endswith('e'):
        return verb[:-1] + 'ing'
    elif (len(verb) >= 3 and
          verb[-1] not in vowels and
          verb[-2] in vowels and
          verb[-3] not in vowels):
        return verb + verb[-1] + 'ing'
    else:
        return verb + 'ing'


# 测试
test_verbs = ['lie', 'see', 'move', 'hug', 'die', 'run', 'fix', 'open', 'make']
for v in test_verbs:
    print(f"{v} -> {make_ing_form(v)}")
