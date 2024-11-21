# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import json
# import ollama
# print("=======================================")
# #print(ollama.list())

# app = Flask(__name__)
# CORS(app)  # 允许跨域访问

# # 用于存储每个用户的聊天记录
# session_messages = {}
# @app.route("/", methods=["GET"])
# def home():
#     return jsonify({"message": "Welcome to the Chat API! Use POST /chat to interact."})



#     try:
#         # 从请求中解析数据
#         data = request.json
#         session_id = data.get("session_id")  # 用于区分用户会话
#         user_message = data.get("message")  # 用户输入
#         model_name = data.get("model_name", "deepseek-coder:6.7b")  # 模型名称，默认 llama3.1

#         # 如果没有 session_id，返回错误
#         if not session_id:
#             return jsonify({"error": "session_id is required"}), 400

#         # 初始化当前用户的会话记录
#         if session_id not in session_messages:
#             session_messages[session_id] = []

#         # 构造模型上下文
#         context = '你是一位友善的老师，帮助学生理解问题。'

#         # 添加用户消息到会话记录
#         session_messages[session_id].append({"role": "user", "content": user_message})

#         # 准备发送给模型的消息
#         messages_to_send = [{"role": "system", "content": context}]
#         messages_to_send.extend(session_messages[session_id])

#         # 调用模型
#         full_response = ""
#         print("Messages to send:", messages_to_send)  # 调试输出
#         for chunk in ollama.chat(model=model_name, messages=messages_to_send, stream=False):
#             print("Chunk received:", chunk)  # 调试输出
#             if isinstance(chunk, dict) and 'message' in chunk and 'content' in chunk['message']:
#                 full_response += chunk['message']['content']
#             else:
#                 print("Invalid chunk format:", chunk)

#         # 检查是否生成了内容
#         if not full_response:
#             full_response = "模型未生成任何响应，请检查输入或模型配置。"

#         # 将助手的回复添加到会话记录中
#         session_messages[session_id].append({"role": "assistant", "content": full_response})

#         # 返回响应
#         return jsonify({
#             "response": full_response,
#             "session_messages": session_messages[session_id]
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     try:
#         # 从请求中解析数据
#         data = request.json
#         session_id = data.get("session_id")  # 用于区分用户会话
#         user_message = data.get("message")  # 用户输入
#         model_name = data.get("model_name", "llama3.1:latest")  # 模型名称，默认 llama3.1

#         # 如果没有 session_id，返回错误
#         if not session_id:
#             return jsonify({"error": "session_id is required"}), 400

#         # 初始化当前用户的会话记录
#         if session_id not in session_messages:
#             session_messages[session_id] = []

#         # 构造模型上下文
#         context = '你是一位友善的老师，帮助学生理解问题'

#         # 添加用户消息到会话记录
#         session_messages[session_id].append({"role": "user", "content": user_message})

#         # 准备发送给模型的消息
#         messages_to_send = [{"role": "system", "content": context}]
#         messages_to_send.extend(session_messages[session_id])

#         # 调用模型
#         full_response = ""
#         for chunk in ollama.chat(model=model_name, messages=messages_to_send, stream=False):
#             try:
#                 # 确保 chunk 是字典类型
#                 if isinstance(chunk, dict) and 'message' in chunk and 'content' in chunk['message']:
#                     full_response += chunk['message']['content']
#                 else:
#                     print("Unexpected chunk format:", chunk)
#             except Exception as e:
#                 print(f"Error processing chunk: {e}")

#         # 将助手的回复添加到会话记录中
#         session_messages[session_id].append({"role": "assistant", "content": full_response})

#         # 返回响应
#         return jsonify({
#             "response": full_response,
#             "session_messages": session_messages[session_id]
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     try:
#         # 从请求中解析数据
#         data = request.json
#         session_id = data.get("session_id")  # 用于区分用户会话
#         user_message = data.get("message")  # 用户输入
#         model_name = data.get("model_name", "llama3.1:latest")  # 模型名称，默认 llama3.1

#         # 如果没有 session_id，返回错误
#         if not session_id:
#             return jsonify({"error": "session_id is required"}), 400

#         # 初始化当前用户的会话记录
#         if session_id not in session_messages:
#             session_messages[session_id] = []

#         # 构造模型上下文
#         context = '你是一位总是以苏格拉底式风格回应的老师......'

#         # 添加用户消息到会话记录
#         session_messages[session_id].append({"role": "user", "content": user_message})

#         # 准备发送给模型的消息
#         messages_to_send = [{"role": "system", "content": context}]
#         messages_to_send.extend(session_messages[session_id])

#         # 调用模型
#         full_response = ""
#         for chunk in ollama.chat(model=model_name, messages=messages_to_send, stream=False):
#             if 'message' in chunk and 'content' in chunk['message']:
#                 full_response += chunk['message']['content']

#         # 将助手的回复添加到会话记录中
#         session_messages[session_id].append({"role": "assistant", "content": full_response})

#         # 返回响应
#         return jsonify({
#             "response": full_response,
#             "session_messages": session_messages[session_id]
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
# @app.route("/chat", methods=["POST"])
# def chat():
#     try:
#         # 从请求中解析数据
#         data = request.json
#         session_id = data.get("session_id")
#         user_message = data.get("message").strip()
#         model_name = data.get("model_name", "llama3.1:latest")

#         # 检查模型是否有效
#         available_models = [m['name'] for m in ollama.list()['models']]
#         if model_name not in available_models:
#             return jsonify({"error": f"Model '{model_name}' not found. Available models: {available_models}"}), 400

#         # 初始化用户会话
#         if session_id not in session_messages:
#             session_messages[session_id] = []

#         # 构造上下文和消息
#         context = "你是一位友善的老师，帮助学生回答问题。"
#         session_messages[session_id].append({"role": "user", "content": user_message})
#         messages_to_send = [{"role": "system", "content": context}]
#         messages_to_send.extend(session_messages[session_id])

#         # 调用模型
#         full_response = ""
#         for chunk in ollama.chat(model=model_name, messages=messages_to_send, stream=True):
#             print("Raw chunk:", chunk)  # 打印 chunk 内容
#             if isinstance(chunk, str):
#                 try:
#                     chunk = json.loads(chunk)  # 解析为 JSON
#                 except json.JSONDecodeError:
#                     print("Non-JSON chunk:", chunk)
#                     continue
#             if isinstance(chunk, dict) and 'message' in chunk and 'content' in chunk['message']:
#                 full_response += chunk['message']['content']
#             elif 'done_reason' in chunk:
#                 print("Generation stopped, reason:", chunk['done_reason'])
#                 break
#             else:
#                 print("Skipping invalid chunk:", chunk)

#         # 检查是否生成了内容
#         if not full_response:
#             full_response = "模型未生成任何响应，请检查输入或模型配置。"

#         # 更新会话记录
#         session_messages[session_id].append({"role": "assistant", "content": full_response})

#         # 返回响应
#         return jsonify({
#             "response": full_response,
#             "session_messages": session_messages[session_id]
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/history", methods=["GET"])
# def get_history():
#     session_id = request.args.get("session_id")

#     if not session_id:
#         return jsonify({"error": "session_id is required"}), 400

#     if session_id not in session_messages:
#         return jsonify({"error": "No chat history found for this session_id"}), 404

#     return jsonify({"session_messages": session_messages[session_id]})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5002, debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import ollama

app = Flask(__name__)
CORS(app)  # Allow cross-origin access

# Used to store chat history for each user
session_messages = {}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Chat API! Use POST /chat to interact."})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Parse data from the request
        data = request.json
        session_id = data.get("session_id")
        user_message = data.get("message").strip()
        model_name = data.get("model_name", "llama3.1:latest")

        # Check if the model is valid
        available_models = [m['name'] for m in ollama.list()['models']]
        if model_name not in available_models:
            return jsonify({"error": f"Model '{model_name}' not found. Available models: {available_models}"}), 400

        # Initialize user session if not already done
        if session_id not in session_messages:
            session_messages[session_id] = []

        # Construct the context and messages
        context = "你是一位友善的老师，帮助学生回答问题。"
        session_messages[session_id].append({"role": "user", "content": user_message})
        messages_to_send = [{"role": "system", "content": context}]
        messages_to_send.extend(session_messages[session_id])

        # Call the model
        full_response = ""
        for chunk in ollama.chat(model=model_name, messages=messages_to_send, stream=True):
            print("Raw chunk:", chunk)  # Debug output
            if isinstance(chunk, str):
                try:
                    chunk = json.loads(chunk)  # Parse as JSON
                except json.JSONDecodeError:
                    print("Non-JSON chunk:", chunk)
                    continue
            if isinstance(chunk, dict) and 'message' in chunk and 'content' in chunk['message']:
                full_response += chunk['message']['content']
            elif 'done_reason' in chunk:
                print("Generation stopped, reason:", chunk['done_reason'])
                break
            else:
                print("Skipping invalid chunk:", chunk)

        # Check if any content was generated
        if not full_response:
            full_response = "模型未生成任何响应，请检查输入或模型配置。"

        # Update session history
        session_messages[session_id].append({"role": "assistant", "content": full_response})

        # Return response
        return jsonify({
            "response": full_response,
            "session_messages": session_messages[session_id]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/history", methods=["GET"])
def get_history():
    session_id = request.args.get("session_id")

    if not session_id:
        return jsonify({"error": "session_id is required"}), 400

    if session_id not in session_messages:
        return jsonify({"error": "No chat history found for this session_id"}), 404

    return jsonify({"session_messages": session_messages[session_id]})

# New route to clear session-specific history
@app.route("/clear_history", methods=["POST"])
def clear_history():
    try:
        data = request.json
        session_id = data.get("session_id")

        if not session_id:
            return jsonify({"error": "session_id is required"}), 400

        if session_id in session_messages:
            del session_messages[session_id]
            return jsonify({"message": "Chat history cleared."}), 200
        else:
            return jsonify({"error": "No chat history found for this session_id"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


    try:
        session_messages.clear()
        return jsonify({"message": "All chat histories cleared."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
