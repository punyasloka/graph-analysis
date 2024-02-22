# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    # app.py (continued)
    import graphviz
    import json


    @app.route('/generate_graph')
    def generate_graph():
        dot_file_path = 'path/to/your/graph.dot'
        graph = graphviz.Source.from_file(dot_file_path, format='png', engine='dot')

        # Convert the graph data to a JSON-like format
        graph_data = {
            'nodes': [{'id': node.replace('"', ''), 'label': node.replace('"', '')} for node in graph.nodes()],
            'edges': [{'source': edge[0].replace('"', ''), 'target': edge[1].replace('"', '')} for edge in
                      graph.edges()]
        }

        with open('static/your_graph_data.js', 'w') as file:
            file.write('const graphData = ' + json.dumps(graph_data) + ';')

        return 'Graph data generated successfully!'


    if __name__ == '__main__':
        app.run(debug=True)
