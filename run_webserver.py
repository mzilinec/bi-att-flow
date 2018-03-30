from squad.demo_prepro import prepro
from basic.demo_cli import Demo

paragraph = "Since age 15 or so, the main goal of professor Jurgen Schmidhuber has been to build a self-improving " \
            "Artificial Intelligence (AI) smarter than himself, then retire. His lab's Deep Learning Neural " \
            "Networks (since 1991) such as Long Short-Term Memory (LSTM) have transformed machine learning and " \
            "AI, and are now (2017) available to billions of users through the world's most valuable public " \
            "companies, Deep Learning since 1991 - Winning Contests in Pattern Recognition and Sequence Learning " \
            "Through Fast & Deep / Recurrent Neural Networks e.g., for greatly improved (CTC-based) speech " \
            "recognition on over 2 billion Android phones (since mid 2015), greatly improved machine translation " \
            "through Google Translate (since Nov 2016) and Facebook (over 4 billion LSTM-based translations per " \
            "day as of 2017), Siri and Quicktype on almost 1 billion iPhones (since 2016), the answers of Amazon's " \
            "Alexa, and numerous other applications. In 2011, his team was the first to win official computer " \
            "vision contests through deep neural nets, with superhuman performance. His research group also " \
            "established the field of mathematically rigorous universal AI and recursive self-improvement in " \
            "universal problem solvers that learn to learn (since 1987). His formal theory of creativity & " \
            "curiosity & fun explains art, science, music, and humor. He also generalized algorithmic " \
            "information theory and the many-worlds theory of physics, and introduced the concept of " \
            "Low-Complexity Art, the information age's extreme form of minimal art. He is recipient of " \
            "numerous awards, and Chief Scientist of the company NNAISENSE, which aims at building the " \
            "first practical general purpose AI."

questions = [
  "What do public companies use?",
  "Who is Jurgen Schmidhuber?",
  "What is NNAISENSE?",
  "Who stole Schmidhuber's ideas?"
]

pq_prepro = prepro(paragraph, questions[0])

demo = Demo()

answers = demo.run(pq_prepro)

print(answers)