# import flask
# from flask import request, jsonify, Blueprint
# import connexion
#
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True
#
#
# cities = [
#     {'id': 0,
#      'city': 'Melbourne'
#      },
#     {'id': 1,
#      'city': 'Sydney'
#      },
#     {'id': 2,
#      'city': 'Brisbane'
#      },
#     {'id': 3,
#      'city': 'Melsss'
#      }
# ]
#
#
# #api = Api(version='1.0', title='My search API',
# #          description='')
# #api.init_app(blueprint)
#
#
# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
#
#
# @app.route('/suggestions', methods=['GET'])
# def api_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'q' in request.args:
#         q = request.args['q']
#     else:
#         return "Error: No search term provided. Please specify a search term."
#
#     # Create an empty list for our results
#     results = []
#
#     # Loop through the data and match results that fit the requested city or string.
#     for city in cities:
#         if q.lower() in city['city'].lower():
#             results.append(city['city'])
#
#     # Use the jsonify function from Flask to convert the list of JSON format
#     return jsonify(results)
#
#
# blueprint = Blueprint('api', __name__, url_prefix='/api')
# app.register_blueprint(blueprint)
# app.run()
