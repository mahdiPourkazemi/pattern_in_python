class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None
    
class AuthHandler(Handler):
    def handle(self, request):
        if request.get('authenticated'):
            print("User authenticated.")
            return super().handle(request)
        else:
            print("Authentication required.")
            return "Authentication failed."
        
class ContentHandler(Handler):
    def handle(self, request):
        if request.get('content') and len(request['content']) > 10:
            print("Content is valid.")
            return super().handle(request)
        else:
            print("Content is too short.")
            return "Content validation failed."
        
class FinalizeHandler(Handler):
    def handle(self, request):
        print("Comment posted successfully.")
        return "Comment posted."
    
if __name__=="__main__":
    # ایجاد هندلرها
    finalize_handler = FinalizeHandler()
    content_handler = ContentHandler(next_handler=finalize_handler)
    auth_handler = AuthHandler(next_handler=content_handler)
    
    # درخواست آزمایشی
    request = {'authenticated': True, 'content': "This is a valid comment."}
    
    # پردازش درخواست
    response = auth_handler.handle(request)
    print(response)