
class Response:


    def __init__(self, data, status=200, message=None):
        self.data = data
        self.status = status
        self. message = message


    def to_dict(self):
        http_success_status = {
            100: 'Continue',
            101: 'Switching Protocols',
            103: 'Early Hints',
            200: 'OK',
            201: 'Created',
            202: 'Accepted',
            203: 'Non-Authoritative Information',
            204: 'No Content',
            205: 'Reset Content',
            206: 'Partial Content',
            300: 'Multiple Choices',
            301: 'Moved Permanently',
            302: 'Found',
            303: 'See Other',
            304: 'Not Modified',
            307: 'Temporary Redirect',
            308: 'Permanent Redirect'
        }

        response = {
            'data': self.data,
            'message': self.message if self.message else http_success_status.get(self.status, ''),
            'status': self.status
        }
        return response, self.status
