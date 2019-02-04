from functools import wraps

from flask import make_response, jsonify

class HttpController:
    def __repr__(self):
        """Print descriptions of this class.
        """
        return "HttpController.response_json()"

    @staticmethod
    def response_json(fun=None):
        """Response the JSON's format.
        """
        @wraps(fun)
        # wraps can assist internal function to get parameters.
        def wrapper(*args, **kwds):
            try:
                results, total = fun(*args, **kwds)
                if not results:
                    return jsonify(message="Data is empty!"), 404

                r = make_response(jsonify(data=results, total=total), 200)
                r.add_etag()
                return r
            except Exception as e:
                return jsonify(message=str(repr(e))), 404

        return wrapper
