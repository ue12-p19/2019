from nbautoeval import Quiz, QuizQuestion, Option, CodeOption, MathOption, MarkdownOption
from nbautoeval import TextContent, MarkdownContent

# NOTE à propos de markdown
# dans cette première question j'avais dans un premier
# temps utilisé un bloc entre ```
# et il s'avère que ça marchouille seulement
# 
# à terme on pourrait imaginer utiliser une autre librairie 
# de markdown, je pense à celui de jupyter notebook...

# common score
SCORE = 4

questions = []


#
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On a besoin d'écrire un programme très gourmand en calcul; 
le problème se découpe bien en morceaux indépendant les uns des autres;
on veut absolument utiliser Python pour écrire ce programme;
on dispose d'une machine avec 64 processeurs, et on essaie de se débrouiller
pour les utiliser au mieux.
<br>Cochez les options qui sont raisonnables dans ce contexte :
"""),
#    question2="",
    options=[
        MarkdownOption("""
on crée autant de processus que 
de morceaux, en assemblant les résultats à la fin
""", correct=True),
        MarkdownOption("""
on crée autant de threads que 
de morceaux, en assemblant les résultats à la fin
"""),
        MarkdownOption("""
on crée autant de coroutines que de morceaux, on synchronise les résultats 
grâce à `asyncio.gather` et ainsi on peut assembler les résultats
"""),
    ],
))


#
questions.append(
QuizQuestion(
    score=SCORE,
        question=MarkdownContent(
"""
Indiquer, parmi les opérations suivantes, 
celles qui sont susceptibles d'induire un délai sensible dans du code synchrone,
et que vous pourriez avoir intérêt à gérer de manière asynchrone pour 
rendre votre application plus efficace ou plus réactive :
"""),
    question2="",
    options=[
        MarkdownOption("accès réseau", correct=True),
        MarkdownOption("attente d'événements liés à des sous-process", correct=True),
        MarkdownOption("temporisation/attente volontaire", correct=True),
        MarkdownOption("accès au disque dur ou base de données", correct=True),
        MarkdownOption("accès à la mémoire vive"),
        MarkdownOption("accès au terminal", correct=True),
    ],
))


# 
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On considère le code suivant :

***

    import asyncio

    async def foo():
        await asyncio.sleep(1)
        print("done")
        return 42
        
    x = foo()
"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python;
    <br> cochez parmi les assertations suivantes 
    <br> celles qui vraies à la fin de de l'exécution
    """),
    options=[
        MarkdownOption("rien n'est affiché", correct=True),
        MarkdownOption("le programme a affiché `done`"),
        MarkdownOption("la variable `x` vaut `42`"),
        MarkdownOption("(l'objet référencé par) la variable `x` est awaitable", correct=True),
        MarkdownOption("rien ne s'exécute, à cause d'une erreur de syntaxe"),
    ],
    horizontal_layout=True,
))


# 
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On considère le code suivant :

***

    import asyncio

    async def foo():
        await asyncio.sleep(0.1)
        return 42

    async def bar():
        await asyncio.sleep(0.05)
        return 58

    async def both():
        return await asyncio.gather(foo(), bar())

    results = asyncio.run(both())
    print(results[0])
"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python;
    <br> cochez parmi les assertations suivantes 
    <br> celles qui vraies à la fin de de l'exécution
    """),
    options=[
        MarkdownOption("le programme affiche `42`", correct=True),
        MarkdownOption("le programme dure 100ms", correct=True),
        MarkdownOption("le programme affiche `58`"),
        MarkdownOption("le programme dure 150ms"),
        MarkdownOption("le programme dure 50ms"),
        MarkdownOption("rien ne s'exécute, à cause d'une erreur"),
    ],
    horizontal_layout=True,
))


# 
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
On considère le code suivant :

***

    import asyncio

    async def foo():
        await asyncio.sleep(0.1)
        return 42

    async def bar():
        await asyncio.sleep(0.05)
        return 58

    async def one():
        return await asyncio.wait(
            [foo(), bar()],
            return_when=asyncio.FIRST_COMPLETED)

    done, pending = asyncio.run(one())

    one_done = done.pop()
    print(one_done.result())
"""),
    question2=TextContent("""
    On exécute ce code dans un interpréteur python;
    <br> cochez parmi les assertations suivantes 
    <br> celles qui vraies à la fin de de l'exécution
    """),
    options=[
        MarkdownOption("le programme affiche `42`"),
        MarkdownOption("le programme dure 100ms"),
        MarkdownOption("le programme affiche `58`", correct=True),
        MarkdownOption("le programme dure 150ms"),
        MarkdownOption("le programme dure 50ms", correct=True),
        MarkdownOption("rien ne s'exécute, à cause d'une erreur"),
    ],
    horizontal_layout=True,
))


#
'''
questions.append(
QuizQuestion(
    score=SCORE,
    question=MarkdownContent(
"""
"""),
    question2="",
    options=[
        MarkdownOption(""),
    ],
))
'''


quiz = Quiz(
    "asyncio",
    max_attempts=4,
    questions=questions,
    max_grade=20,
    shuffle=False,
)

