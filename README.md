# Custom version of BiDAF #

## Setup ##

1. Install required Python packages and all.

2. Download pre-trained model from [this link](https://drive.google.com/drive/u/1/folders/12i0OV8Xq99KBRTbEa_ETnWIgLV0f9OVv)
and extract it in the root directory of the project. You will need to move the folders so that you have ./out/basic/...

3. (Optional) Put additional contexts in the **./data/contexts** directory. Each context should be a JSON file with
a "text" key that contains the context. If you want to turn any mess into a one line string, use [this website](https://www.textfixer.com/tools/remove-line-breaks.php)
with the "Remove line breaks and paragraph breaks" option.

## Usage ##

Run the web server.
```
python run-webserver.py
```

Send a **POST** request with the context and the question in the body as a JSON.

endpoint: **http://host:port/question**

example body:
```
{
    "context": "schmidhuber",
    "question": "Who is Jurgen Schmidhuber?"
}
```

**Name of the context** is the name of its JSON file without the .json suffix.

Run the webserver with a different port and address:
```
python run-webserver.py --address 1.1.1.1 --port 2000
```