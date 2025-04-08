from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    pod_name = os.environ.get('POD_NAME', 'unknown')
    node_name = os.environ.get('NODE_NAME', 'unknown')
    namespace = os.environ.get('POD_NAMESPACE', 'unknown')
    return f"Container EDU | POD Working : {pod_name} | nodename : {node_name} | namespace : {namespace}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
