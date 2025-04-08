from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    pod_name = os.environ.get('POD_NAME', 'unknown')
    node_name = os.environ.get('NODE_NAME', 'unknown')
    namespace = os.environ.get('POD_NAMESPACE', 'unknown')
    return f"""
    <h1>Hello from Downward API!</h1>
    <p><b>Pod:</b> {pod_name}</p>
    <p><b>Node:</b> {node_name}</p>
    <p><b>Namespace:</b> {namespace}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
