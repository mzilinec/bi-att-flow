import argparse, os, json
from flask import Flask, request, jsonify
from squad.demo_prepro import prepro
from basic.demo_cli import Demo


# load contexts
CONTEXTS_PATH = "./data/contexts"
TEXT_KEY = "text"
CONTEXT_KEY = "context"
QUESTION_KEY = "question"

if not os.path.isdir(CONTEXTS_PATH):
  raise FileNotFoundError("Contexts directory not found.")

context_files = os.listdir(CONTEXTS_PATH)

if len(context_files) == 0:
  raise FileNotFoundError("No contexts found.")

contexts = {}
for context_file in context_files:

  context_path = os.path.join(CONTEXTS_PATH, context_file)
  context_name = ".".join(context_file.split(".")[:-1])

  with open(context_path, "r") as file:
    context = json.load(file)

  if TEXT_KEY not in context:
    raise ValueError("Text not found in {:s}. Use \"{:s}\" key to supply text in the JSON file."
                     .format(context_path, TEXT_KEY))

  contexts[context_name] = context[TEXT_KEY]

# setup flask app and the model
app = Flask(__name__)
demo = Demo()

def getAnswer(paragraph, question):

  pq_prepro = prepro(paragraph, question)

  if len(pq_prepro['x']) > 1000:
    return "[Error] Sorry, the number of words in paragraph cannot be more than 1000."

  if len(pq_prepro['q']) > 100:
    return "[Error] Sorry, the number of words in question cannot be more than 100."

  return demo.run(pq_prepro)

@app.route("/question", methods=["POST"])
def submit():

    body = request.get_json(silent=True)

    question = body[QUESTION_KEY]
    context = body[CONTEXT_KEY]

    if context not in contexts:
      return jsonify(result="[Error] Invalid context.")

    answer = getAnswer(contexts[context], question)

    return jsonify(result=answer)


if __name__ == "__main__":

    parser = argparse.ArgumentParser("Run a question-answering web server.")

    parser.add_argument("--host", default="0.0.0.0", help="web server host")
    parser.add_argument("--port", type=int, default=1995, help="web server port")

    args = parser.parse_args()

    app.run(host=args.host, port=args.port, threaded=True)
