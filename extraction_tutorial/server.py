"""
Python HTTP server for GraphQL.
"""
from flask import Flask
from flask_graphql import GraphQLView
from flask import request
from schema import schema, extract

application = Flask(__name__)
application.add_url_rule('/',
                 view_func=GraphQLView.as_view('graphql',
                                               schema=schema,
                                               graphiql=True))

@application.route('/extract_page/<path:url>', methods=['GET', 'POST'])
def extract_page(url):
    extracted = extract(url)
    return f"{url}\n{extracted.title}\n{extracted.description}"

if __name__ == '__main__':
    application.config.from_object('configurations.DevelopmentConfig')
    application.run(host='0.0.0.0')
