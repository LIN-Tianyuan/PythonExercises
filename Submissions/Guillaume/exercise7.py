"""Français:
Écrire une version d'un outil de reconnaissance de palindromes qui
qui accepte également les phrases palindromes telles que « Go hang a salami I'm a lasagna hog »,
« C'est un rat que j'ai vu ? », “Ne marchez pas sur les animaux”, “Assieds-toi sur une casserole, Otis”,
« Lisa Bonet n'a pas mangé de basilic », “Satan, fais osciller mes sonates métalliques”,
« J'ai erré en dessous comme un Maori nu et fatigué », “Levez-vous pour voter monsieur”,
ou l'exclamation « Bon sang, je suis fou ! ».
Notez que la ponctuation, les majuscules et les espaces sont généralement ignorés."""


class PalindromeChecker:
    def __init__(self):
        pass

    def _clean_string(self, text: str) -> str:

        accents = {"é": "e", "è": "e", "à": "a", "ù": "u", "ç": "c", "ê": "e"}
        text = text.lower()

        for acc, repo in accents.items():
            text = text.replace(acc, repo)

        cleaned = ""
        for char in text:
            if char.isalnum():
                cleaned += char

        return cleaned

    def check(self, text: str) -> bool:
        cleaned = self._clean_string(text)

        return cleaned == cleaned[::-1]


def verify_phrase(checker: PalindromeChecker, phrase: str):
    if checker.check(phrase):
        print(f" VRAI : « {phrase} » est un palindrome.")
    else:
        print(f"FAUX : « {phrase} » n'est pas un palindrome.")



my_checker = PalindromeChecker()

verify_phrase(my_checker, "Go hang a salami I'm a lasagna hog")
verify_phrase(my_checker, "Was it a rat I saw?")
verify_phrase(my_checker, "Step on no pets")
print("-" * 30)

verify_phrase(my_checker, "Engage le jeu que je le gagne")
verify_phrase(my_checker, "Tu l'as trop écrasé, César, ce Port-Salut !")