from flask import jsonify

class ApiResponse:
    @staticmethod
    def send(success=False, message='Message', data=None, status_code=200):
        response = {
            'success': success, 
            'message': message,
            'data': data
        }
        return jsonify(response), status_code
