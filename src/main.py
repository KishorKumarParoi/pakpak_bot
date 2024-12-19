from flask import Flask, request, jsonify
import json
from helper.openai_api import text_completion, generate_image
from helper.telegram_api import sendMessage, sendPhoto

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home route that returns a greeting message.

    Returns:
        str: A greeting message "Hello, Flask!".
    """
    return "Hello, Flask!"


@app.route("/telegram", methods=["POST"])
def telegram():
    """
    Telegram route that processes JSON data from a POST request and returns a greeting message.

    Returns:
        tuple: A tuple containing a greeting message "Hello, Telegram!" and a status code 200.
    """
    try:
        data = request.get_json()
        print(json.dumps(data))
        message = data.get("message", {})
        query = message.get("text", "")
        chat_id = message.get("chat", {}).get("id", "")

        if not query or not chat_id:
            return jsonify({"status": 0, "error": "Invalid message format"}), 400

        print(f"Received message: {query} from chat_id: {chat_id}")

        # response = text_completion(query)
        # sendMessage(chat_id, response["response"])

        words = query.split(" ")
        if words[0] == "/img":
            image_response = generate_image(" ".join(words[1:]))
            sendPhoto(chat_id, image_response["url"], "Generated Image by OpenAI")
        elif words[0] == "/ask":
            text_response = text_completion(" ".join(words[1:]))
            sendMessage(chat_id, text_response["response"])
        else:
            sendMessage(
                chat_id,
                "Please use /img or /ask commands to generate an image or ask a question.",
            )
        return jsonify({"status": 1, "message": "Request processed successfully"}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"status": 0, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5002)
